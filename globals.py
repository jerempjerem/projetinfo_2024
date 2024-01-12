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


PRENOM_UTILISATEUR : str = "" # Prénom de l'utilisateur authentifié
USERNAME_UTILISATEUR : str = "" # Nom d'utilisateur de l'utilisateur authentifié
NOMBRE_HEURES_UTILISATEUR : float = 0 # Nombre d'heure du contrat de l'utilisateur authentifié
EQUIPES_GEREES_UTILISATEUR : dict[list] = {} # Dictionnaire de toutes les équipes gerées par l'utilsateur et la liste des personnes de l'equipe associé
PERSONNE_GEREE_USER : list = [] # Liste des personnes gerées par l'utilisateur authentifié

EVENT_LIEUX : list = [] # Liste de tous les lieux existant dans la bdd
EVENT_TYPES_AND_COLORS : dict = {} # Dictionnaire de tous les types d'evenement et leurs couleur associé
PERSONNES : list = [] # Liste de toutes les personnes existantes dans la bdd
EQUIPES_DB : dict = {} # Dictionnaire de toutes les équipes existantes dans la bdd et la liste des personnes de l'équipe associé

CURRENT_EDITED_EVENT_ID = None # Variable qui nous permets de recuperer l'id de l'evenement qui est en train d'etre modifié

EVENT_KEYS = ["Id", "Nom", "Place", "StartTime", "EndTime", "EventType"] # Constante des clés qui compose le dictionnaires qui defini un evenement

TYPE_EVENT_VACANCES = ['Conges']

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

