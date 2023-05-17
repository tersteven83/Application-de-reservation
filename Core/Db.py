import sys

import psycopg2


class Db:
    def __init__(self):
        global connection
        try:
            # connexion au server
            self._connection = psycopg2.connect(user="typhon",
                                                password="typhon",
                                                host="127.0.0.1",
                                                port="5432",
                                                database="projet_python")
            # on met en place le curseur
            # curseur peut etre accéder par les descendants de Db
            # self._curseur = connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print(f"Failed to connect to database: {error}")
            sys.exit(1)

    def _getConnection(self):
        """
        cette fonction retourne le curseur après la connexion à la base de donnée
        :return: self
        """
        return self._connection
