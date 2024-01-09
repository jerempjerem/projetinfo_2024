from database import Database
import tempfile
import os

db = Database()

TEMPFILE_NAME = "planning_session"
PATH_TEMP_FILE = os.path.join(tempfile.gettempdir(), f"{TEMPFILE_NAME}.json")


PRENOM_UTILISATEUR = ""
USERNAME_UTILISATEUR = ""

PLANNING_TABS = {
    'Planning': [],
    'Editer': []
}

JOURS_NUMEROTES = {
    "lundi": 1,
    "mardi": 2,
    "mercredi": 3,
    "jeudi": 4,
    "vendredi": 5,
    "samedi": 6,
    "dimanche": 7
}

HEURES_NUMEROTES = {
    '8': 0,
    '9': 2,
    '10': 4,
    '11': 6,
    '12': 8,
    '13': 10,
    '14': 12,
    '15': 14,
    '16': 16,
    '17': 18,
}

