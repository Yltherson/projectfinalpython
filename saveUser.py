from database import connectiondb as con


class Registre:

    @staticmethod
    def save(user):
        userData = (user.getFullName(), user.getAge(), user.getNumero(), user.getEmail(), user.getFact())
        sql = "insert into etudiants(fullName, age, numero, email, fact) values(?, ?, ?, ?, ?)"
        conect = con()
        cur = conect.cursor()
        cur.execute(sql, userData)

        conect.commit()
        conect.close()
