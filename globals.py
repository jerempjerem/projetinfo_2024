########################################################################
# Ce fichier permet de stocker les variables constante et/ou les 
# variables qu'on utilise dans plusieurs fichiers/fonctions
# differentes et de pouvoir y acceder facilement sans probleme de porté
# de variables
########################################################################

########################################################################
# IMPORT LIBRARIES
import tempfile
import os
########################################################################


########################################################################
# IMPORT FILES
from database import Database
########################################################################

db = Database()

# Nom et chemin du fichier utilisé pour stocker la session de l'utilisateur authentifié
TEMPFILE_NAME = "planning_session"
PATH_TEMP_FILE = os.path.join(tempfile.gettempdir(), f"{TEMPFILE_NAME}.json")


PRENOM_UTILISATEUR = ""
USERNAME_UTILISATEUR = ""
NOMBRE_HEURES_UTILISATEUR = 0
EQUIPES_UTILISATEUR = {}
PERSONNE_GEREE_USER = []

EVENT_LIEUX = []
EVENT_TYPES_AND_COLORS = {}
EQUIPES = []
PERSONNES = ()
EQUIPES_DB = {}

CURRENT_EDITED_EVENT_ID = None

EVENT_KEYS = ["Id", "Nom", "Place", "StartTime", "EndTime", "EventType"]

ROLES_ID = {
    "collaborateur": 1,
    "Manager": 0,
}

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
    '08': 0,
    '09': 2,
    '10': 4,
    '11': 6,
    '12': 8,
    '13': 10,
    '14': 12,
    '15': 14,
    '16': 16,
    '17': 18,
}

