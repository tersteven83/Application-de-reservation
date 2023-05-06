from Core.Db import Db


class Model(Db):
    curseur = None
    table = None
    id = None

    def __init__(self):
        super().__init__()

    def requete(self, sql, attributs=None):
        """
        Faire une requête
        :param sql: sql pur ou en format
        :param attributs:
        :return: doit être suivis par les fetch dans l'emploi
        """
        self.curseur = self.getCurseur()

        if attributs is None:
            self.curseur.execute(sql)
            return self.curseur
        else:
            self.curseur.execute(sql, attributs)
            return self.curseur

    def findAll(self):
        return self.requete(f"SELECT * FROM {self.table}").fetchall()

    def find(self, id):
        return self.requete(f"SELECT * FROM {self.table} WHERE id={id}").fetchone()

    def findBy(self, criteres):
        # Critere doit etre en type dictionary
        # SELECT * FROM tabName WHERE col1=val1 AND col2=val2 AND col3=val3
        # on explode le dictionnaire d'abord
        liste_des_cols = []  # ce liste de col doit etre de la forme col1=%s AND col2=%s....
        liste_des_vals = []
        for key, value in criteres.items():
            liste_des_cols.append(key + '=%s')  # dans la boucle, c'est encore de la forme de liste
            liste_des_vals.append(value)
        # on doit merge la liste en string par le séparateur 'AND'
        cols = " AND ".join(liste_des_cols)

        return self.requete(f"SELECT * FROM {self.table} WHERE {cols}", liste_des_vals).fetchall()


    def modifier(self, criteres):
        # UPDATE tabName SET col1=val1, col=val2 WHERE id=?
        liste_des_cols = []
        liste_des_vals = []
        for key, value in criteres.items:
            liste_des_cols.append(key + "=%s")
            liste_des_vals.append(value)
        cols = " ,".join(liste_des_cols)

        return self.requete(f"UPDATE {self.table} SET {cols} WHERE id={self.id}", liste_des_vals)

    def create(self, criteres):
        # INSERT INTO tabName(col1,col2,...) VALUES(val1,val2,...)
        # de la forme VALUES(%s, %s, %s,...) qui dépend du nombre de cols
        liste_des_cols = []
        liste_des_vals = []
        liste_format = []
        for key, value in criteres.items():
            liste_des_cols.append(key)
            liste_des_vals.append(value)
            liste_format.append('%s')
        cols = ','.join(liste_des_cols)
        formatstring = ','.join(liste_format)
        return self.requete(f"INSERT INTO {self.table}({cols}) VALUES({formatstring})", liste_des_vals)

    def supprimer(self, id):
        # DELETE FROM tabName WHERE id=?
        return self.requete(f"DELETE FROM {self.table} WHERE id={id}")


    def hydrate(self, criteres):
        """
        criteres est un dictionnaire key:value
        on ajoute le mot 'set' devant key=>setKey
        si setKey existe dans l'objet instancié, on affecte sa valeur pas value
        sinon on ne fait rien
        :param criteres:
        :return:
        """
        for key, value in criteres.items():
            setter = 'set' + key.capitalize()
            if hasattr(self, setter) and callable(self.setter):
                self.setter(value)
        return self
