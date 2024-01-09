import tempfile
import json
import os

# Spécifier un préfixe pour le nom du fichier temporaire
filename = "mon_fichier_json"
path_temp_file = os.path.join(tempfile.gettempdir(), f"{filename}.json")

# Vérifier si le fichier temporaire JSON existe
if os.path.exists(path_temp_file):
    # Si le fichier existe, le lire et imprimer son contenu
    with open(path_temp_file, 'r') as existing_file:
        contenu_existant = json.load(existing_file)
        print(f"Contenu existant dans le fichier temporaire : {contenu_existant}")
else:
    # Si le fichier n'existe pas, créer le fichier et écrire le contenu JSON
    donnees_json = {"nom": "John", "age": 30, "ville": "Paris"}
    with open(path_temp_file, 'w') as new_file:
        json.dump(donnees_json, new_file, indent=2)
        print(f"Le fichier JSON temporaire {path_temp_file} a été créé.")

