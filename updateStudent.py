from database import connectiondb as con


class Modifier:
    @staticmethod
    def update(user):
        userData = (user.getFullName(), user.getAge(), user.getNumero(), user.getEmail(), user.getFact(), user.getEmail(), id)
        sql = "update etudiants set fullName = (?), age = (?), numero = (?), email = (?), fact = (?) where email = (?)"
        conect = con()
        cur = conect.cursor()
        cur.execute(sql, userData)

        conect.commit()
        conect.close()
