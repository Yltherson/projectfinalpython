from tkinter import *
from showStudent import Afficher


def afficher(fram6):
    rs = Afficher.show()
    rsl = rs.fetchall()

    for et in rsl:
        Label(fram6, text=f'{et[0]} {et[1]} {et[2]} {et[3]} {et[4]}').pack()
