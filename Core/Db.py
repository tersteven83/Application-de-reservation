import psycopg2
from keyring.backends import null


class Db:
    instance = null
    DBHOST = 'localhost'
    DBUSER = 'typhon'
    DBPASS = 'typhon'
    DBNAME = 'projet_python'

    def __init__(self):
        global connection
        try:
            # on appelle le psycopg2
            connection = psycopg2.connect(user=self.DBUSER, password=self.DBPASS, host=self.DBHOST, database=self.DBNAME, port='5432')
            #maka curseur le instance
            self.instance = connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print(f"Failed to connect to database: {error}")
        finally:
            if connection:
                connection.commit()
                self.instance.close()
                connection.close()


    def getInstance(self):
        if self.instance == null:
            self.__class__()
        return self.instance


