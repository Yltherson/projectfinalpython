from tkinter import *
from user import User
from saveUser import Registre


def enregistrer(fram3):
    nameL = Label(fram3, text="Nom Complet")
    nameE = Entry(fram3, width=20)

    ageL = Label(fram3, text="Age")
    ageE = Entry(fram3, width=20)

    numL = Label(fram3, text="Telephone")
    numE = Entry(fram3, width=20)

    mail = Label(fram3, text="Email")
    mailE = Entry(fram3, width=20)

    factL = Label(fram3, text="Faculte")
    factE = Entry(fram3, width=20)

    def tst():
        if (mailE.get()):
            student = User(nameE.get(), ageE.get(), numE.get(), mailE.get(), factE.get())
            Registre.save(student)

    btn = Button(fram3, text='ENREGISTRER', command=tst)


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
