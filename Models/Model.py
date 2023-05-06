from keyring.backends import null

from Core.Db import Db


class Model(Db):
    db = null
    table = ''

    def __init__(self):
        super().__init__()
        self.bd = None

    def requete(self, sql, attributs=null):
        self.db = super().getInstance()

        if attributs != null:
            return self.bd.execute(sql, attributs)
        else:
            return self.db.execute(sql)
