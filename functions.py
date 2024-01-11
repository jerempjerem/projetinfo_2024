from datetime import datetime , timedelta
# from main import MainWindow, LoginDialog
import os
import sys
import globals
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import json
import hashlib

def read_user():
    with open(globals.PATH_TEMP_FILE, 'r') as existing_file:
        content = json.load(existing_file)
        globals.PRENOM_UTILISATEUR = content['Prenom'] 
        globals.USERNAME_UTILISATEUR = content['Username']
        globals.NOMBRE_HEURES_UTILISATEUR = content['NbHeure']

def save_user():
    data = {"Prenom": globals.PRENOM_UTILISATEUR, "Username": globals.USERNAME_UTILISATEUR, "NbHeure": globals.NOMBRE_HEURES_UTILISATEUR}
    with open(globals.PATH_TEMP_FILE, 'w') as new_file:
        json.dump(data, new_file, indent=2)

def get_teams_managed_user():
    print(globals.USERNAME_UTILISATEUR)
    query = """
        SELECT EQUIPE.Nom
        FROM EMPLOYES
        INNER JOIN PARTICIPANT_G ON EMPLOYES.EmployesID= PARTICIPANT_G.EmployesID_ext2
        INNER JOIN EQUIPE ON PARTICIPANT_G.EquipeID_ext = EQUIPE.EquipeID
        INNER JOIN ROLE ON PARTICIPANT_G.RoleID_ext = ROLE.RoleID
        WHERE EMPLOYES.Username = %s AND ROLE.RoleID = 0;
    """
    result = [element[0] for element in globals.db.fetch(query, (globals.USERNAME_UTILISATEUR,))]
    globals.EQUIPES_UTILISATEUR = {equipe: None for equipe in result}
    
    personne_geree_user = []
    for equipe in result:
        query = """
            SELECT EMPLOYES.Username
            FROM EMPLOYES
            INNER JOIN PARTICIPANT_G ON EMPLOYES.EmployesID= PARTICIPANT_G.EmployesID_ext2
            INNER JOIN EQUIPE ON PARTICIPANT_G.EquipeID_ext = EQUIPE.EquipeID
            INNER JOIN ROLE ON PARTICIPANT_G.RoleID_ext = ROLE.RoleID
            WHERE EQUIPE.Nom=%s
            ORDER BY ROLE.RoleID
        """
    
        result = [element[0] for element in globals.db.fetch(query, (equipe,))]
        
        personne_geree_user += result
        globals.EQUIPES_UTILISATEUR[equipe] = result
    
    globals.PERSONNE_GEREE_USER = element_distinct_list(personne_geree_user)
def element_distinct_list(liste: list) -> list:
    return list(set(liste))

def hasher_mot_de_passe(mot_de_passe):
    hasher = hashlib.sha256()
    hasher.update(mot_de_passe.encode('utf-8'))
    hash_resultat = hasher.hexdigest()
    return hash_resultat

class MainController():
    def __init__(self, parent) -> None:
        self.parent = parent
                
    def update_calendar(self, plage_label: QLabel, calendar_labels: list[QLabel], table: QTableWidget, tab: str, previous_week : bool = False, next_week : bool = False, option_date: str = None):
        # Changement des dates afficher
        table.clearContents()
        table.clearSpans()
        
        if option_date:
            date = option_date
        else:
            date = globals.PLANNING_TABS[tab][0]
            
        if tab == 'Planning':
            iseditable = False
            user_selected = globals.USERNAME_UTILISATEUR
        elif tab == 'Editer':
            iseditable = True
            user_selected = self.parent.ui.editpersonpicker.currentText()
        else:
            iseditable = False
            user_selected = None
                    
        globals.PLANNING_TABS[tab] = self._get_weekdates(date, previous_week=previous_week, next_week=next_week) # On recupere le calendrier de la semaine pour un jour donnée

        calendar_dates = self._get_calendar_dates(globals.PLANNING_TABS[tab]) # On recupere les dates affiche sur les colonnes de la table
        planning_plage = self._get_plage_dates(globals.PLANNING_TABS[tab]) # On recupere la plage des dates de la semaine selectionné
        
        [calendar_labels[i].setText(calendar_dates[i]) for i in range(len(calendar_labels))]
        plage_label.setText(planning_plage)
        
        # Changement des evenements
        total_heures_semaine = 0
        for event in self._get_all_event_user(globals.PLANNING_TABS[tab], user_selected):
            duration = self._get_event_duration(event['StartTime'], event['EndTime'])
            hours = f"{event['StartTime'].strftime('%H:%M')} - {event['EndTime'].strftime('%H:%M')}"
            colonne, ligne = self._get_event_position(event['StartTime'])
            
            self._add_event(table, colonne, ligne, duration, hours, event, iseditable)
            total_heures_semaine += round(duration/2, 1)
        
        if tab == 'Planning':
            self.parent.ui.planningnbheures.setText(f"Nombre d'heures : {total_heures_semaine}/{globals.NOMBRE_HEURES_UTILISATEUR}")
            if total_heures_semaine <= globals.NOMBRE_HEURES_UTILISATEUR:
                self.parent.ui.planningnbheures.setStyleSheet('color: green')
            else:
                self.parent.ui.planningnbheures.setStyleSheet('color: red')
            
    def displaypopup(self, event: dict = None, iseditable : bool = False):
        self.parent.ui.popupteams.clearSelection()
        self.parent.ui.popuppersons.clearSelection()
        self.parent.ui.popuplieux.clear()
        self.parent.ui.popuptype.clear()
        
        if event:
            globals.CURRENT_EDITED_EVENT_ID = event['Id']
            personnes, equipes = self._equipe_et_personnes_event(event['Id'])

            if iseditable:
                self._edit_popup(event['Nom'], event['StartTime'], event['EndTime'], element_distinct_list([event['Place']] + globals.EVENT_LIEUX),
                                 element_distinct_list(equipes + globals.EQUIPES), element_distinct_list(personnes + globals.PERSONNES),
                                 element_distinct_list([event['EventType']] + list(globals.EVENT_TYPES_AND_COLORS.keys())))
                self._set_popup_to_writeonly()
            else:
                self._edit_popup(event['Nom'], event['StartTime'], event['EndTime'], [event['Place']], equipes, personnes, list(globals.EVENT_TYPES_AND_COLORS.keys()))
                self._set_popup_to_readonly()
        else:
            date_debut = datetime.now()
            date_fin = date_debut+timedelta(hours=2)
            
            lieux_dispo, personne_dispo, equipes_dispo = self._lieu_equipe_personne_dispo(date_debut, date_fin)

            self._edit_popup("Nom de l'event", date_debut, date_fin, lieux_dispo, equipes_dispo, personne_dispo, list(globals.EVENT_TYPES_AND_COLORS.keys()))

            
        self.parent.ui.popupContainer.expandMenu()    
        
    def save_edit_event(self):
        event_name = self.parent.ui.popupeventname.text()
        date_debut = self.parent.ui.popupdatedebut.dateTime().toPython()
        date_fin = self.parent.ui.popupdatefin.dateTime().toPython()
        lieu = self.parent.ui.popuplieux.currentText()
        event_type = self.parent.ui.popuptype.currentText()
        equipes = [item.text() for item in self.parent.ui.popupteams.selectedItems()]
        personnes = [item.text() for item in self.parent.ui.popuppersons.selectedItems()]

        if lieu not in globals.EVENT_LIEUX:
            # Ajouter dans la BDD
            globals.EVENT_LIEUX.append(lieu)
            
        if event_type not in list(globals.EVENT_TYPES_AND_COLORS.keys()):
            # Ajouter dans la BDD
            globals.EVENT_LIEUX.append(lieu)
            
        if globals.CURRENT_EDITED_EVENT_ID is not None:
            # Event existant on le modifie dans la BDD
            self._edit_existing_event(event_name, date_debut, date_fin, lieu, event_type, globals.CURRENT_EDITED_EVENT_ID)
        else :
            # Nouvel event on l'ajoute a la BDD    
            self._ajouter_un_evenement(equipes + personnes, event_name, date_debut, date_fin, lieu, event_type)       
        
        # refresh le planning d edit
        self._refresh_table_edit()
        self.parent.ui.popupContainer.collapseMenu()

    def edit_popup_on_date_change(self, date_debut: datetime, date_fin: datetime):

        lieux_dispo, personne_dispo, equipes_dispo = self._lieu_equipe_personne_dispo(date_debut, date_fin)

        self.parent.ui.popuplieux.clear()
        self.parent.ui.popuppersons.clear()
        self.parent.ui.popupteams.clear()
        
        self.parent.ui.popuplieux.addItems(lieux_dispo)
        self.parent.ui.popuppersons.addItems(personne_dispo)
        self.parent.ui.popupteams.addItems(equipes_dispo)

    def change_persons(self):
        self.parent.ui.editpersonpicker.clear()
        self.parent.ui.editpersonpicker.addItems(globals.EQUIPES_UTILISATEUR[self.parent.ui.editeteampicker.currentText()])
    
    def close_popup(self):
        self.parent.ui.popupContainer.collapseMenu()
        globals.CURRENT_EDITED_EVENT_ID = None
              
    def _get_event_position(self, startTime: datetime) -> (int, int):
        jour = startTime.strftime("%A")
        colonne = globals.JOURS_NUMEROTES[jour] - 1
        
        heure = startTime.strftime("%H")
        ligne = globals.HEURES_NUMEROTES[heure]
        
        return colonne, ligne
        
    def _get_all_event_user(self, calendar_week: list, user_selected: str) -> list[dict]:
        
        query = """
            SELECT EVENEMENT.EvenementID, EVENEMENT.Nom, LIEU.Nom, EVENEMENT.DateDebut, EVENEMENT.DateFin, TYPE.Nom, EMPLOYES.Prenom
            FROM EMPLOYES
            INNER JOIN PARTICIPANT_G ON EMPLOYES.EmployesID=PARTICIPANT_G.EmployesID_ext2
            INNER JOIN EQUIPE ON PARTICIPANT_G.EquipeID_ext=EQUIPE.EquipeID
            INNER JOIN PARTICIPANT_E ON EQUIPE.EquipeID=PARTICIPANT_E.EquipeID_ext2
            INNER JOIN EVENEMENT ON PARTICIPANT_E.EvenementID_ext2=EVENEMENT.EvenementID
            INNER JOIN TYPE ON EVENEMENT.TypeID_ext = TYPE.TypeID
            INNER JOIN LIEU ON EVENEMENT.LieuID_ext=LIEU.LieuID
            WHERE EMPLOYES.UserName=%s AND EVENEMENT.DateDebut BETWEEN %s and %s

            UNION

            SELECT EVENEMENT.EvenementID, EVENEMENT.Nom, LIEU.Nom, EVENEMENT.DateDebut, EVENEMENT.DateFin, TYPE.Nom, EMPLOYES.Prenom
            FROM EMPLOYES
            INNER JOIN PARTICIPANT_P ON EMPLOYES.EmployesID=PARTICIPANT_P.EmployesID_ext
            INNER JOIN EVENEMENT ON PARTICIPANT_P.EvenementID_ext=EVENEMENT.EvenementID
            INNER JOIN TYPE ON EVENEMENT.TypeID_ext = TYPE.TypeID
            INNER JOIN LIEU ON EVENEMENT.LieuID_ext=LIEU.LieuID
            WHERE EMPLOYES.UserName=%s AND EVENEMENT.DateDebut BETWEEN %s and %s
        """
        params = (user_selected, datetime.strptime(calendar_week[0], "%d/%m/%Y").strftime("%Y-%m-%d"), datetime.strptime(calendar_week[-1], "%d/%m/%Y").strftime("%Y-%m-%d"))

        evenements = globals.db.fetch(query, params+params)
        
        return self._format_list_events([dict(zip(globals.EVENT_KEYS, event)) for event in evenements])

    def _get_event_duration(self, debut: datetime, fin: datetime) -> int:
        # Calculer la différence entre les deux dates
        duree = fin - debut

        # Convertir la différence en heures et minutes
        heures, reste = divmod(duree.seconds, 3600)
        minutes = reste // 60

        duration = 2*heures if minutes < 30 else 2*heures + 1 # Sur le plannig 1 heure fait 2 cases
        return duration
        
    def _get_calendar_dates(self, dates : list[str]) -> list:
        dates_formatees = []
        jours_semaine = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']

        for date_str in dates:
            # Conversion de la chaîne en objet datetime
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            
            # Création de la nouvelle chaîne au format 'Jour JJ'
            nouvelle_date_str = '{} {}'.format(jours_semaine[date_obj.weekday()], date_obj.strftime('%d'))
            
            dates_formatees.append(nouvelle_date_str)
        return dates_formatees

    def _get_weekdates(self, date: str, previous_week: bool = False, next_week: bool = False) -> list[str]:
        """Par default renvoi la semaine actuelle"""        
        dates = []
        
        formatage_date = datetime.strptime(date, "%d/%m/%Y")     
        nom_jour = formatage_date.strftime("%A")               
        nb_jour = globals.JOURS_NUMEROTES[nom_jour]
        
        if previous_week:
            week = formatage_date - timedelta(days=nb_jour+7)
        elif next_week:
            week = formatage_date + timedelta(days=7-nb_jour)
        else:
            week = formatage_date - timedelta(days=nb_jour)

        dates = [(week + timedelta(days=i+1)).strftime("%d/%m/%Y") for i in range(7)]
            
        return dates

    def _get_plage_dates(self, dates: list[str]) -> str:
        
        start_date = datetime.strptime(dates[0], "%d/%m/%Y").strftime("%d %B")
        end_date = datetime.strptime(dates[-1], "%d/%m/%Y").strftime("%d %B %Y")
        
        return f"{start_date} - {end_date}"
    
    def _create_event_item(self, hours: str, duration: int, event: dict, isEditable: bool = False):
        # Fonts
        font = QFont()
        font.setFamily(u"Sans Serif Collection")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        
        font2 = QFont()
        font2.setFamily(u"Sans Serif Collection")
        font2.setPointSize(8)

        # Widget contenant les infos
        widget = QWidget()
        widget.setStyleSheet(u"QWidget{\n"
        f"	background-color: {globals.EVENT_TYPES_AND_COLORS[event['EventType']]};\n"
        "	border-top-left-radius: 10px;\n"
        "	border-top-right-radius: 10px;\n"
        "	border-bottom-left-radius: 10px;\n"
        "	border-bottom-right-radius: 10px;\n"
        "}")
        verticalLayout = QVBoxLayout(widget)
        verticalLayout.setSpacing(0)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # Frame du haut contenant le nom de l'activité
        frame = QFrame(widget)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        verticalLayout_2 = QVBoxLayout(frame)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        label_activite = QLabel(event['Nom'], frame)
        label_activite.setFont(font)
        label_activite.setAlignment(Qt.AlignCenter)
        
        verticalLayout_2.addWidget(label_activite)
        verticalLayout.addWidget(frame)
        
        if duration >= 3:
            # Frame du milieu contenant le nom de les heures et le lieu
            frame_2 = QFrame(widget)
            frame_2.setFrameShape(QFrame.StyledPanel)
            frame_2.setFrameShadow(QFrame.Raised)
            horizontalLayout_2 = QHBoxLayout(frame_2)
            horizontalLayout_2.setSpacing(3)
            horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
            label_heure = QLabel(hours, frame_2)
            label_heure.setAlignment(Qt.AlignCenter)
            label_heure.setFont(font2)

            horizontalLayout_2.addWidget(label_heure)

            label_lieu = QLabel(event['Place'], frame_2)
            label_lieu.setAlignment(Qt.AlignCenter)
            label_lieu.setFont(font2)


            horizontalLayout_2.addWidget(label_lieu)

            verticalLayout.addWidget(frame_2)
        
        # Frame du bas contenant le bouton detail
        frame_3 = QFrame(widget)
        frame_3.setFrameShape(QFrame.StyledPanel)
        frame_3.setFrameShadow(QFrame.Raised)
        horizontalLayout_3 = QHBoxLayout(frame_3)
        horizontalLayout_3.setSpacing(5)
        horizontalLayout_3.setContentsMargins(0, 0, 10, 10)
        
        if isEditable:
            deleteeventBtn = QPushButton(frame_3)
            deleteeventBtn.setCursor(QCursor(Qt.PointingHandCursor))
            icon2 = QIcon()
            icon2.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
            deleteeventBtn.setIcon(icon2)
            deleteeventBtn.setIconSize(QSize(15, 15))
            deleteeventBtn.clicked.connect(lambda: self._delete_event(event['Id']))
            
            horizontalLayout_3.addWidget(deleteeventBtn)
            
            editeventBtn = QPushButton(frame_3)
            editeventBtn.setCursor(QCursor(Qt.PointingHandCursor))
            icon2 = QIcon()
            icon2.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
            editeventBtn.setIcon(icon2)
            editeventBtn.setIconSize(QSize(15, 15))
            editeventBtn.clicked.connect(lambda: self.displaypopup(event, iseditable=True))
            
            horizontalLayout_3.addWidget(editeventBtn)
        
        detailsBtn = QPushButton(frame_3)
        detailsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        detailsBtn.setIcon(icon)
        detailsBtn.setIconSize(QSize(15, 15))
        detailsBtn.clicked.connect(lambda: self.displaypopup(event))
        
        horizontalLayout_3.addWidget(detailsBtn)
        

        verticalLayout.addWidget(frame_3, 0, Qt.AlignRight|Qt.AlignBottom)
        
        return widget

    def _add_event(self, table: QTableWidget, colonne: int, ligne: int, duration: int, hours: str, event : dict, isEditable: bool = False):
        # Création de l'item personnalisé
        custom_widget = self._create_event_item(hours, duration, event, isEditable)

        # Création de l'item de tableau personnalisé
        item = QTableWidgetItem()
        
        # Définition du widget comme élément de la cellule
        table.setSpan(ligne, colonne, duration, 1)
        table.setCellWidget(ligne, colonne, custom_widget)
        table.setItem(ligne, colonne, item)

    def _format_list_events(self, all_events: list) -> list:
        events = []
        for event in all_events:
            if self._is_long_event(event):
                events.extend(self._split_event_by_day(event))
            else:
                events.append(event)
        return events

    def _is_long_event(self, event: dict) -> bool:
        # Garder que les dates des evenements sans les heures
        start_date_part = event['StartTime'].date()
        end_date_part = event['EndTime'].date()
        
        # Comparer les parties de date
        if start_date_part == end_date_part:
            return False
        else:
            return True
    
    def _split_event_by_day(self, event: dict):
        events_list = []

        start_time = event['StartTime']
        end_time = event['EndTime']
        start_day = start_time.date()
        end_day = end_time.date()

        while start_day <= end_day:
            # Créer un nouvel événement pour chaque jour
            new_event = event.copy()
            new_event['StartTime'] = max(start_time, datetime.combine(start_day, datetime.min.time()) + timedelta(hours=8))
            new_event['EndTime'] = min(end_time, datetime.combine(start_day, datetime.min.time()) + timedelta(hours=18))
            events_list.append(new_event)

            # Passer au jour suivant
            start_day += timedelta(days=1)
            
        return events_list
       
    def _set_popup_to_writeonly(self):
        self.parent.ui.popupeventname.setReadOnly(False)
        self.parent.ui.popupdatedebut.setReadOnly(False)
        self.parent.ui.popupdatefin.setReadOnly(False)
        self.parent.ui.popuplieux.setEnabled(True)
        self.parent.ui.popuptype.setEnabled(True)
        self.parent.ui.popupteams.setSelectionMode(QListWidget.MultiSelection)
        self.parent.ui.popuppersons.setSelectionMode(QListWidget.MultiSelection)   
        
    def _set_popup_to_readonly(self):
        self.parent.ui.popupeventname.setReadOnly(True)
        self.parent.ui.popupdatedebut.setReadOnly(True)
        self.parent.ui.popupdatefin.setReadOnly(True)
        self.parent.ui.popuplieux.setEnabled(False)
        self.parent.ui.popuptype.setEnabled(False)
        self.parent.ui.popupteams.setSelectionMode(QListWidget.NoSelection)
        self.parent.ui.popuppersons.setSelectionMode(QListWidget.NoSelection)
        
    def _equipe_et_personnes_event(self, eventID: int) -> (list, list):
        query = """
            SELECT EMPLOYES.Username, EQUIPE.Nom 
            FROM EMPLOYES 
            INNER JOIN PARTICIPANT_G ON EMPLOYES.EmployesID = PARTICIPANT_G.EmployesID_ext2 
            INNER JOIN EQUIPE ON PARTICIPANT_G.EquipeID_ext = EQUIPE.EquipeID 
            INNER JOIN PARTICIPANT_E ON EQUIPE.EquipeID = PARTICIPANT_E.EquipeID_ext2 
            INNER JOIN EVENEMENT ON PARTICIPANT_E.EvenementID_ext2 = EVENEMENT.EvenementID 
            WHERE EVENEMENT.EvenementID = %s 
            
            UNION 
            
            SELECT EMPLOYES.Username, NULL 
            FROM EMPLOYES 
            INNER JOIN PARTICIPANT_P ON EMPLOYES.EmployesID = PARTICIPANT_P.EmployesID_ext 
            INNER JOIN EVENEMENT ON PARTICIPANT_P.EvenementID_ext = EVENEMENT.EvenementID 
            WHERE EVENEMENT.EvenementID = %s; 
        """
        
        resultats = globals.db.fetch(query, (eventID, eventID))
        
        personnes = element_distinct_list([element[0] for element in resultats])
        equipes = element_distinct_list([element[1] for element in resultats if element[1] is not None])
        return personnes, equipes 
       
    def _edit_popup(self, event_name: str, date_debut: datetime, date_fin: datetime, lieux: list, equipes: list, personnes: list, types: list):
        self.parent.ui.popupeventname.setText(event_name)
        self.parent.ui.popupdatedebut.setDateTime(date_debut)
        self.parent.ui.popupdatefin.setDateTime(date_fin)
        self.parent.ui.popuplieux.addItems(lieux)
        self.parent.ui.popuptype.addItems(types)
        self.parent.ui.popupteams.addItems(equipes)
        self.parent.ui.popuppersons.addItems(personnes)
        
    def _edit_existing_event(self, event_name, date_debut, date_fin, lieu, event_type, event_id):
        lieu_id : list[tuple] = globals.db.fetch("SELECT LIEU.LieuID FROM LIEU WHERE LIEU.Nom = %s", (lieu,))
        type_id : list[tuple] = globals.db.fetch("SELECT TYPE.TypeID FROM TYPE WHERE TYPE.Nom = %s", (event_type,))

        query = """
            UPDATE EVENEMENT
            SET EVENEMENT.Nom=%s, EVENEMENT.DateDebut=%s, EVENEMENT.DateFin=%s, EVENEMENT.LieuID_ext=%s, EVENEMENT.TypeID_ext = %s
            WHERE EVENEMENT.EvenementID = %s ;
        """
        
        params = (event_name,  date_debut, date_fin, lieu_id[0][0], type_id[0][0], event_id)
        
        globals.db.edit(query, params)
    
    def _ajouter_un_evenement(self, liste_personnes_equipes: list, event_name:str, date_debut: datetime, date_fin: datetime, lieu: str, event_type: str):
        compteur = globals.db.fetch("SELECT MAX(EvenementID) FROM EVENEMENT ")
        lieu_id : list[tuple] = globals.db.fetch("SELECT LIEU.LieuID FROM LIEU WHERE LIEU.Nom = %s", (lieu,))
        type_id : list[tuple] = globals.db.fetch("SELECT TYPE.TypeID FROM TYPE WHERE TYPE.Nom = %s", (event_type,))

        query = "INSERT INTO EVENEMENT (EvenementID, Nom, DateDebut, DateFin, LieuID_ext, TypeID_ext) VALUES (%s, %s, %s, %s, %s,%s)"
        params = (compteur[0][0] + 1, event_name , date_debut, date_fin, lieu_id[0][0], type_id[0][0])
        print(params)
        globals.db.edit(query, params)

        for personne in liste_personnes_equipes:
            # Chercher dans la table GROUPE
            resultats_groupe = globals.db.fetch(f"SELECT EquipeID FROM EQUIPE WHERE Nom = '{personne}'")

            # Chercher dans la table EMPLOYES
            resultats_employe = globals.db.fetch(f"SELECT EmployesID FROM EMPLOYES WHERE Username = '{personne}'")

            # Insérer dans la table PARTICIPANT_E ou PARTICIPANT_P en fonction du type de résultat
            if resultats_groupe !=[]:
                for resultat in resultats_groupe:
                    globals.db.edit("INSERT INTO PARTICIPANT_E (EvenementID_ext2, EquipeID_ext2) VALUES (%s, %s)",(compteur[0][0] + 1, resultat[0]))
            if resultats_employe!=[]:
                for resultat in resultats_employe:
                    globals.db.edit("INSERT INTO PARTICIPANT_P (EvenementID_ext, EmployesID_ext) VALUES (%s, %s)",(compteur[0][0] + 1, resultat[0]))
    
    def _delete_event(self, event_id: int):

        query = [
            "DELETE FROM PARTICIPANT_P WHERE PARTICIPANT_P.EvenementID_ext = %s;", 
            "DELETE FROM PARTICIPANT_E WHERE PARTICIPANT_E.EvenementID_ext2 = %s;", 
            "DELETE FROM EVENEMENT WHERE EVENEMENT.EvenementID = %s;"
        ]
        
        for q in query:
            globals.db.edit(q, (event_id,))
            
        self._refresh_table_edit()
        
    def _refresh_table_edit(self):
        self.update_calendar(self.parent.ui.editsemaine, self.parent.editcalendar, self.parent.ui.tableedit, 'Editer')
            
    def _lieux_disponible(self, date_debut: datetime, date_fin: datetime) -> list:
        query = """
            SELECT LIEU.Nom
            FROM LIEU

            EXCEPT

            SELECT LIEU.Nom
            FROM LIEU
            INNER JOIN EVENEMENT ON LIEU.LieuID = EVENEMENT.LieuID_ext

            WHERE (
                (EVENEMENT.DateDebut BETWEEN %s AND %s) OR (EVENEMENT.DateFin BETWEEN %s AND %s) 
                OR 
                (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin) OR (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin)
            )
        """
        
        params = (date_debut, date_fin, date_debut, date_fin, date_debut, date_fin)
        
        result = [element[0] for element in globals.db.fetch(query, params)]
        
        return result

    def _personnes_disponible(self, date_debut : datetime, date_fin : datetime) -> list:

        #Analyse des date debut et fin
        #requete sql afin d'obtenir un tuple avec la liste des personnes libre.
        
        query = """
            SELECT EMPLOYES.Username
            FROM EMPLOYES

            EXCEPT

            SELECT EMPLOYES.Username
            FROM FONCTION
            INNER JOIN EMPLOYES ON FONCTION.FonctionID=EMPLOYES.FonctionID_ext
            INNER JOIN PARTICIPANT_G ON EMPLOYES.EmployesID=PARTICIPANT_G.EmployesID_ext2
            INNER JOIN EQUIPE ON PARTICIPANT_G.EquipeID_ext=EQUIPE.EquipeID
            INNER JOIN PARTICIPANT_E ON EQUIPE.EquipeID=PARTICIPANT_E.EquipeID_ext2
            INNER JOIN EVENEMENT ON PARTICIPANT_E.EvenementID_ext2=EVENEMENT.EvenementID
            WHERE (
                (EVENEMENT.DateDebut BETWEEN %s AND %s) OR (EVENEMENT.DateFin BETWEEN %s AND %s) 
                OR 
                (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin) OR (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin)
            )

            EXCEPT

            SELECT EMPLOYES.Username
            FROM EVENEMENT
            INNER JOIN PARTICIPANT_P ON EVENEMENT.EvenementID=PARTICIPANT_P.EvenementID_ext
            INNER JOIN EMPLOYES ON PARTICIPANT_P.EmployesID_ext=EMPLOYES.EmployesID
            INNER JOIN FONCTION ON EMPLOYES.FonctionID_ext=FONCTION.FonctionID
            WHERE (
                (EVENEMENT.DateDebut BETWEEN %s AND %s) OR (EVENEMENT.DateFin BETWEEN %s AND %s) 
                OR 
                (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin) OR (%s BETWEEN EVENEMENT.DateDebut AND EVENEMENT.DateFin)
            )
        """
        params = (date_debut, date_fin, date_debut, date_fin, date_debut, date_fin, date_debut, date_fin, date_debut, date_fin, date_debut, date_fin)
        
        personne_libre = [element[0] for element in globals.db.fetch(query, params)]
        
        return list(set(personne_libre) & set(globals.PERSONNE_GEREE_USER))
    
    def _equipe_libre(self, personne_libre: list) -> list:
        equipes_libre = []
        
        for equipe, personne_equipe in globals.EQUIPES_DB.items():
            
            intersection_personne = set(personne_equipe) & set(personne_libre) 
            
            if intersection_personne == set(personne_equipe):
                equipes_libre.append(equipe)
                
        return list(set(equipes_libre) & set(globals.EQUIPES_UTILISATEUR))
    
    def _lieu_equipe_personne_dispo(self, date_debut : datetime, date_fin : datetime) -> (list, list, list):
        lieux_dispo = self._lieux_disponible(date_debut, date_fin)  
        personne_dispo = self._personnes_disponible(date_debut, date_fin)
        equipes_dispo = self._equipe_libre(personne_dispo)
        return lieux_dispo, personne_dispo, equipes_dispo
    
    
class LoginController():
    def __init__(self, parent) -> None:
        self.parent = parent
        
    def login(self):
            query = f"SELECT UserName, Mdp, Prenom, NbHeure FROM EMPLOYES WHERE Username='{self.parent.ui.username.text()}'"
            result = globals.db.fetch(query)

            if result:
                hashed_password = result[0][1]
                globals.PRENOM_UTILISATEUR = result[0][2]
                globals.USERNAME_UTILISATEUR = result[0][0]
                globals.NOMBRE_HEURES_UTILISATEUR = float(result[0][3])
                
                if hashed_password == hasher_mot_de_passe(self.parent.ui.password.text()):
                    self.parent.accept()
                else:
                    self.parent.ui.password.clear()
                    self.parent.ui.error_password.setText("Mot de passe invalide")
            else:
                self.parent.ui.username.clear()
                self.parent.ui.password.clear()
                self.parent.ui.error_password.setText("Nom d'utilisateur invalide")
                