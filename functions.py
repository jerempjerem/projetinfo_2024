from datetime import datetime , timedelta
import os
import sys
import globals
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import json

def read_user():
    with open(globals.PATH_TEMP_FILE, 'r') as existing_file:
        content = json.load(existing_file)
        globals.PRENOM_UTILISATEUR = content['Prenom'] 
        globals.USERNAME_UTILISATEUR = content['Username']

def save_user():
    data = {"Prenom": globals.PRENOM_UTILISATEUR, "Username": globals.USERNAME_UTILISATEUR}
    with open(globals.PATH_TEMP_FILE, 'w') as new_file:
        json.dump(data, new_file, indent=2)

def element_distinct_list(liste: list) -> list:
    return list(set(liste))


class MainController():
    def __init__(self, parent : QMainWindow) -> None:
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
        for event in self._get_all_event_user(globals.PLANNING_TABS[tab], user_selected):
            duration = self._get_event_duration(event['StartTime'], event['EndTime'])
            hours = f"{event['StartTime'].strftime('%H:%M')} - {event['EndTime'].strftime('%H:%M')}"
            colonne, ligne = self._get_event_position(event['StartTime'])
            
            self._add_event(table, colonne, ligne, duration, hours, event, iseditable)
            
    def displaypopup(self, event: dict = None, iseditable : bool = False):
        self.parent.ui.popupteams.clearSelection()
        self.parent.ui.popuppersons.clearSelection()
        self.parent.ui.popuplieux.clear()

        if event and iseditable:
            self._edit_popup(event['Nom'], event['StartTime'], event['EndTime'], element_distinct_list([event['Place']] + globals.EVENT_LIEUX))
            self._set_popup_to_writeonly()
        elif event and not iseditable:
            self._edit_popup(event['Nom'], event['StartTime'], event['EndTime'], [event['Place']])
            self._set_popup_to_readonly()
        else:
            self._edit_popup("Nom de l'event", datetime.now(), datetime.now(), globals.EVENT_LIEUX, globals.EQUIPES, globals.PERSONNES)

            
        self.parent.ui.popupContainer.expandMenu()        
              
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
        
        keys = ["Id", "Nom", "Place", "StartTime", "EndTime", "EventType"]

        return self._format_list_events([dict(zip(keys, event)) for event in evenements])

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
        "	background-color: rgb(214, 240, 255);\n"
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
        self.parent.ui.popupteams.setSelectionMode(QListWidget.MultiSelection)
        self.parent.ui.popuppersons.setSelectionMode(QListWidget.MultiSelection)   
        
    def _set_popup_to_readonly(self):
        self.parent.ui.popupeventname.setReadOnly(True)
        self.parent.ui.popupdatedebut.setReadOnly(True)
        self.parent.ui.popupdatefin.setReadOnly(True)
        self.parent.ui.popuplieux.setEnabled(False)
        self.parent.ui.popupteams.setSelectionMode(QListWidget.NoSelection)
        self.parent.ui.popuppersons.setSelectionMode(QListWidget.NoSelection)
        
    def _edit_popup(self, event_name: str, date_debut: datetime, date_fin: datetime, lieux: list, equipes: list = [], personnes: list = []):
        self.parent.ui.popupeventname.setText(event_name)
        self.parent.ui.popupdatedebut.setDateTime(date_debut)
        self.parent.ui.popupdatefin.setDateTime(date_fin)
        self.parent.ui.popuplieux.addItems(lieux)
        
class LoginController():
    def __init__(self, parent : QDialog) -> None:
        self.parent = parent
        
    def login(self):
            query = f"SELECT UserName, Mdp, Prenom FROM EMPLOYES WHERE Username='{self.parent.ui.username.text()}'"
            result = globals.db.fetch(query)
            
            if result:
                password = result[0][1]
                globals.PRENOM_UTILISATEUR = result[0][2]
                globals.USERNAME_UTILISATEUR = result[0][0]
                
                if password == self.parent.ui.password.text():
                    self.parent.accept()
                else:
                    self.parent.ui.password.clear()
                    self.parent.ui.error_password.setText("Mot de passe invalide")
            else:
                self.parent.ui.username.clear()
                self.parent.ui.password.clear()
                self.parent.ui.error_password.setText("Nom d'utilisateur invalide")
                