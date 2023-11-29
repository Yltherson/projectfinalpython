from tkinter import *


def edit(fram4):
    nameL = Label(fram4, text="Nom Complet")
    nameE = Entry(fram4, width=20)

    ageL = Label(fram4, text="Age")
    ageE = Entry(fram4, width=20)

    numL = Label(fram4, text="Telephone")
    numE = Entry(fram4, width=20)

    mail = Label(fram4, text="Email")
    mailE = Entry(fram4, width=20)

    factL = Label(fram4, text="Faculte")
    factE = Entry(fram4, width=20)

    btn = Button(fram4, text='MODIFIER')

    # position
    nameL.grid(row=0, column=0)
    nameE.grid(row=0, column=1)

    ageL.grid(row=1, column=0)
    ageE.grid(row=1, column=1)

    numL.grid(row=2, column=0)
    numE.grid(row=2, column=1)

    mail.grid(row=3, column=0)
    mailE.grid(row=3, column=1)

    factL.grid(row=4, column=0)
    factE.grid(row=4, column=1)

    btn.grid(row=5, column=1)
