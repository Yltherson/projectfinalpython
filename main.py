from tkinter import *
from tkinter import Tk

root = Tk()

enregistreL = Label(root, text="Enregistrer un etudiant", justify="center")
afficherL = Label(root, text="Afficher etudiants", justify="center")
modifierL = Label(root, text="Modifier etudiant", justify="center")
rechercherL = Label(root, text="Rechercher un etudiant", justify="center")
supprimerL = Label(root, text="Supprimer un etudiant", justify="center")


enregistreL.grid(row=0, column=0)
afficherL.grid(row=1, column=0)
modifierL.grid(row=2, column=0)
rechercherL.grid(row=3, column=0)
supprimerL.grid(row=4, column=0)

root.mainloop()
