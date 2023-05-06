import psycopg2


class Db:
    def __init__(self):
        global connection
        try:
            # connexion au server
            connection = psycopg2.connect(user="typhon",
                                          password="typhon",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="projet_python")
            # on met en place le curseur
            self.curseur = connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print(f"Failed to connect to database: {error}")
        finally:
            if connection:
                connection.commit()


    def getCurseur(self):
        """
        cette fonction retourne le curseur après la connexion à la base de donnée
        :return: self
        """
        return self.curseur




