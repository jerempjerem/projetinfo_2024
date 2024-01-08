import mysql.connector
cnx = mysql.connector.connect(user='342615', password='Projet1nfo!',host='mysql-pierre-jean.alwaysdata.net',database='pierre-jean_projet2024')
moncurseur = cnx.cursor()



def login(username,password):
    
    requête ="SELECT * FROM EMPLOYES "
    moncurseur.execute(requête)
    resultats = moncurseur.fetchall()
    for resultat in resultats:
        if username == resultat[-2] and password == resultat[-1]:
            return True

    return False


