from datetime import datetime , timedelta
import globals
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class MainController():
    def __init__(self, parent : QMainWindow) -> None:
        self.parent = parent
        
        self.planningcalendar : list[QLabel] = [self.parent.ui.planninglundi, self.parent.ui.planningmardi, self.parent.ui.planningmercredi, self.parent.ui.planningjeudi, self.parent.ui.planningvendredi, self.parent.ui.planningsamedi, self.parent.ui.planningdimanche]
        
    def updates_planning_week(self, plage_label: QLabel, date: str, previous_week : bool = False, next_week : bool = False):
        globals.planning_week = self._get_weekdates(date, previous_week=previous_week, next_week=next_week)
        
        calendar_dates = self._get_calendar_dates(globals.planning_week)
        planning_plage = self._get_plage_dates(globals.planning_week)
        
        [self.planningcalendar[i].setText(calendar_dates[i]) for i in range(len(self.planningcalendar))]
        plage_label.setText(planning_plage)

    def _get_calendar_dates(self, dates : list[str]):
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
        
        JOURS_NUMEROTES = {
            "lundi": 1,
            "mardi": 2,
            "mercredi": 3,
            "jeudi": 4,
            "vendredi": 5,
            "samedi": 6,
            "dimanche": 7
        }
        
        dates = []
        
        formatage_date = datetime.strptime(date, "%d/%m/%Y")     
        nom_jour = formatage_date.strftime("%A")               
        nb_jour = JOURS_NUMEROTES[nom_jour]
        
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

    def _create_custom_table_item(self, label1_text, label2_text, button_text, button_callback):
        # Création d'un widget pour contenir les deux labels et le bouton
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Création des labels
        label1 = QLabel(label1_text)
        label2 = QLabel(label2_text)

        # Création du bouton
        button = QPushButton(button_text)
        button.clicked.connect(button_callback)

        # Ajout des widgets au layout
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(button)

        # Ajustement du layout
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        return widget
    
    def _test(self):
        widget = QWidget()
        widget.setStyleSheet(u"QWidget{\n"
        "	background-color: rgb(214, 240, 255);\n"
        "	border-top-left-radius: 10px;\n"
        "	border-top-right-radius: 10px;\n"
        "	border-bottom-left-radius: 10px;\n"
        "	border-bottom-right-radius: 10px;\n"
        "}")
        
        verticalLayout = QVBoxLayout(widget)
        frame = QFrame(widget)

        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        horizontalLayout = QHBoxLayout(frame)
        label_4 = QLabel(frame)
        label_4.setText('Activité')
        label_4.setAlignment(Qt.AlignCenter)

        horizontalLayout.addWidget(label_4)


        verticalLayout.addWidget(frame)

        frame_2 = QFrame(widget)
        frame_2.setFrameShape(QFrame.StyledPanel)
        frame_2.setFrameShadow(QFrame.Raised)
        horizontalLayout_2 = QHBoxLayout(frame_2)
        label_3 = QLabel(frame_2)
        label_3.setText('10h-12H')

        horizontalLayout_2.addWidget(label_3)

        label = QLabel(frame_2)
        label.setText('C406')

        horizontalLayout_2.addWidget(label)


        verticalLayout.addWidget(frame_2)
        
        return widget


class LoginController():
    def __init__(self, parent : QDialog) -> None:
        self.parent = parent
        
    def login(self):
            query = f"SELECT Username, Mdp, Prenom FROM EMPLOYES WHERE Username='{self.parent.ui.username.text()}'"
            result = globals.db.fetch(query)
            
            if result:
                password = result[0][1]
                globals.PRENOM_UTILISATEUR = result[0][2]
                
                if password == self.parent.ui.password.text():
                    self.parent.accept()
                else:
                    self.parent.ui.password.clear()
                    self.parent.ui.error_password.setText("Mot de passe invalide")
            else:
                self.parent.ui.username.clear()
                self.parent.ui.password.clear()
                self.parent.ui.error_password.setText("Nom d'utilisateur invalide")
                