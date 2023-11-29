from tkinter import *


def searchForm(fram5):
    barL = Label(fram5, text="Email")
    barE = Entry(fram5, width=20)

    barL.grid(row=0, column=0)
    barE.grid(row=0, column=1)

    btn = Button(fram5, text='Rechercher')
    btn.grid(row=1, column=1)
