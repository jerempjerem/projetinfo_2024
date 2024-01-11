import mysql.connector

"""
        Fonction permettant de récupérer des données dans une database donnée.

        :param query: requête SQL que l'on veut exécuter
        :return: renvoie les données récupérées grâce à cette requête
        """ 

class Database():

    def __init__(self):
        self.user = '342615'
        self.password = 'Projet1nfo!'
        self.host = 'mysql-pierre-jean.alwaysdata.net'
        self.database = 'pierre-jean_info'
        
    def fetch(self, query: str, params: tuple = ()) -> list[tuple]: # TODO: verifier que la requete s'est bien executé
        """
        Permet de récupérer de selectionné des données dans la bdd

        Args:
            query (str): equête SQL que l'on veut exécuter
            params (tuple, optional): Parametres de la requete. Defaults to ().

        Returns:
            list[tuple]: Données récupérées grâce à la query
        """
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            self.connection.close()
            return result
        
        return []
        
    def edit(self, query: str, variables: tuple = ()): # TODO: verifier que la requete s'est bien executé
        """
        Permet de modfié des données dans la bdd ou d'en inseré

        Args:
            query (str): equête SQL que l'on veut exécuter
            params (tuple, optional): Parametres de la requete. Defaults to ().
        """
        if self.connect():
            cursor = self.connection.cursor()
            cursor.execute(query, variables)
            self.connection.commit()
            cursor.close()
            self.connection.close()

    def connect(self) -> bool:
        """
        Permet de se connecter à la BDD
        
        Returns:
            bool: Indique si la connexion a réussi ouu echoué
        """

        try:
            self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            return True
        except Exception as e:
            self.connection = None
            print(f'Erreur lors de la connexion a la base de donnée: {e}')
            return False


