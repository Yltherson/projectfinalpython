from tkinter import *
from formSave import enregistrer
from editForm import edit
from searchView import searchForm
from showAllView import afficher
from showStudent import Afficher

root2 = Tk()
root2.geometry('1024x600')

fram1 = Frame(master=root2, width=224, bg='gray', border=4, pady=224)
fram2 = Frame(master=root2, width=800, border=4)
fram3 = Frame(master=fram2, border=4)
fram4 = Frame(master=fram2, border=4)
fram5 = Frame(master=fram2, border=4)
fram6 = Frame(master=fram2, border=4)

fram1.pack(side=LEFT,expand=True, fill=BOTH)
fram2.pack(side=RIGHT, expand=True)
fram3.pack()
fram4.pack()
fram5.pack()
fram6.pack()

afficher(fram6)
def clear1():
    fram4.pack_forget()
    fram5.pack_forget()
    fram6.pack_forget()
    fram3.pack()
    enregistrer(fram3)

def clear2():
    fram3.pack_forget()
    fram5.pack_forget()
    fram6.pack_forget()
    fram4.pack()
    edit(fram4)

def clear3():
    fram3.pack_forget()
    fram4.pack_forget()
    fram6.pack_forget()
    fram5.pack()
    searchForm(fram5)


def clear4():
    fram3.pack_forget()
    fram4.pack_forget()
    fram5.pack_forget()
    fram6.pack()


def menu(fram1):

    btn1 = Button(fram1, text='ENREGISTRER', command=clear1)
    btn2 = Button(fram1, text='MODIFIER', command=clear2)
    btn3 = Button(fram1, text='RECHERCHER', command=clear3)
    btn4 = Button(fram1, text='AFFICHER', command=clear4)
    btn5 = Button(fram1, text='SUPPRIMER')

    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()

menu(fram1)
root2.mainloop()
