from datetime import datetime , timedelta
import os
import sys
import globals
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class MainController():
    def __init__(self, parent : QMainWindow) -> None:
        self.parent = parent
                
    def update_calendar(self, plage_label: QLabel, date: str, calendar_labels: list[QLabel], table: QTableWidget, tab: str, previous_week : bool = False, next_week : bool = False):
        # Changement des dates afficher
        table.clear()
        
        globals.PLANNING_TABS[tab] = self._get_weekdates(date, previous_week=previous_week, next_week=next_week) # On recupere le calendrier de la semaine pour un jour donnée
        
        calendar_dates = self._get_calendar_dates(globals.PLANNING_TABS[tab]) # On recupere les dates affiche sur les colonnes de la table
        planning_plage = self._get_plage_dates(globals.PLANNING_TABS[tab]) # On recupere la plage des dates de la semaine selectionné
        
        [calendar_labels[i].setText(calendar_dates[i]) for i in range(len(calendar_labels))]
        plage_label.setText(planning_plage)
        
        # Changement des evenements
        for event in self._get_all_event_user(globals.PLANNING_TABS[tab]):
            duration = self._get_event_duration(event['StartTime'], event['EndTime'])
            hours = f"{event['StartTime'].strftime('%H:%M')} - {event['EndTime'].strftime('%H:%M')}"
            colonne, ligne = self._get_event_position(event['StartTime'])
            
            self._add_event(table, colonne, ligne, duration, event["Nom"], hours, event['Place'], event['Id'], event)
            
    def disconnect(self):
        if os.path.exists(globals.PATH_TEMP_FILE):
            os.remove(globals.PATH_TEMP_FILE)
            
            # puis fermer la fenetre
 
            
    def _get_event_position(self, startTime: datetime) -> (int, int):
        jour = startTime.strftime("%A")
        colonne = globals.JOURS_NUMEROTES[jour] - 1
        
        heure = startTime.strftime("%H")
        ligne = globals.HEURES_NUMEROTES[heure]
        
        return colonne, ligne
        
    def _get_all_event_user(self, calendar_week: list) -> list[dict]:
        query = """
            SELECT EVENEMENT.EvenementID, EVENEMENT.Nom, EVENEMENT.Lieu, EVENEMENT.DateDebut, EVENEMENT.DateFin
            FROM PARTICIPANT_P
            INNER JOIN EMPLOYES ON EMPLOYES.EmployesID = PARTICIPANT_P.EmployesID_ext
            INNER JOIN EVENEMENT ON EVENEMENT.EvenementID = PARTICIPANT_P.EvenementID_ext
            WHERE EMPLOYES.UserName=%s AND EVENEMENT.DateDebut BETWEEN %s and %s
        """
        params = (globals.USERNAME_UTILISATEUR, datetime.strptime(calendar_week[0], "%d/%m/%Y").strftime("%Y-%m-%d"), datetime.strptime(calendar_week[-1], "%d/%m/%Y").strftime("%Y-%m-%d"))

        evenements = globals.db.fetch(query, params)
        keys = ["Id", "Nom", "Place", "StartTime", "EndTime", "Username"]

        return [dict(zip(keys, event)) for event in evenements]

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
    
    def _create_event_item(self, event_name: str, hours: str, place: str, duration: int, eventId: int, event: dict, isEditable: bool = False):
        
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
        label_activite = QLabel(event_name, frame)
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

            label_lieu = QLabel(place, frame_2)
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
            editeventBtn.clicked.connect(lambda: print(event, 'edit'))
            
            horizontalLayout_3.addWidget(editeventBtn)
        
        detailsBtn = QPushButton(frame_3)
        detailsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        detailsBtn.setIcon(icon)
        detailsBtn.setIconSize(QSize(15, 15))
        detailsBtn.clicked.connect(lambda: print(event, 'details'))
        
        horizontalLayout_3.addWidget(detailsBtn)
        

        verticalLayout.addWidget(frame_3, 0, Qt.AlignRight|Qt.AlignBottom)
        
        return widget

    def _add_event(self, table: QTableWidget, colonne: int, ligne: int, duration: int, event_name: str, hours: str, place: str,  eventId: int, isEditable: bool = False):
        # Création de l'item personnalisé
        custom_widget = self._create_event_item(event_name, hours, place, duration, eventId, isEditable)

        # Création de l'item de tableau personnalisé
        item = QTableWidgetItem()
        
        # Définition du widget comme élément de la cellule
        table.setSpan(ligne, colonne, duration, 1)
        table.setCellWidget(ligne, colonne, custom_widget)
        table.setItem(ligne, colonne, item)


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
                