import mysql.connector

class Database():

    def __init__(self):
        self.user = '342615'
        self.password = 'Projet1nfo!'
        self.host = 'mysql-pierre-jean.alwaysdata.net'
        self.database = 'pierre-jean_bdd'
        

    def fetch(self, query: str, params: tuple = ()) -> list:
        """
        Fonction permettant de récupérer des données dans une database donnée.

        :param query: requête SQL que l'on veut exécuter
        :return: renvoie les données récupérées grâce à cette requête
        """ 
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            self.connection.close()
            return result
        
        return []
        
    def edit(self, query: str, variables: tuple = ()):
        """
        Fonction permettant de modifier une database donnée (INSERT, DELETE, CHANGE).

        :param query: requête SQL que l'on veut exécuter
        :param variables: variables de la requete
        """ 
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query, variables)
            self.connection.commit()
            cursor.close()

    def connect(self) -> bool:
        """
        Fonction permettant de se connecter à la database donnée.

        :return: renvoie un booléen True si nous sommes connecté, False sinon
        """ 

        try:
            self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            return True
        except Exception as e:
            self.connection = None
            print(f'Erreur lors de la connexion a la base de donnée: {e}')
            return False


