from database import connectiondb as con


class Supprimer:

    @staticmethod
    def delete(mail):
        userData = (mail,)
        sql = "delete from etudiants where email = (?)"
        conect = con()
        cur = conect.cursor()
        cur.execute(sql, userData)

        conect.commit()
        conect.close()
