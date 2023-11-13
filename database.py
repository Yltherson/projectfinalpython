import sqlite3 as sqlite


def connectiondb():
    con = sqlite.connect("data.db")
    tab = '''create table IF NOT EXISTS etudiants
                    (fullName text, age text, numero text, email text primary key, fact text)'''
    cursor = con.cursor()
    cursor.execute(tab)
    con.commit()

    return con
