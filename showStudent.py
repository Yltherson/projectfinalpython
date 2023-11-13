from database import connectiondb as con


class Afficher:

    @staticmethod
    def show():
        sql = "select * from etudiants"
        conect = con()
        cur = conect.cursor()
        cur.execute(sql)

        return cur
