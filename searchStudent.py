from database import connectiondb as con


class Rechercher:

    @staticmethod
    def search(mail):
        userData = (mail,)
        sql = "select * from etudiants where email = (?)"
        conect = con()
        cur = conect.cursor()
        cur.execute(sql, userData)

        return cur
