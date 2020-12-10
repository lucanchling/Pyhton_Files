# Header
# Pendu version Graphique
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files/tree/main/TP_Pendu
# 10 Décembre 2020
# To Do : Correction de plusieurs bugs (actualisation du mot, gestion du nombre d'essai avec affichage de la photo correspondante, gestion du score... beaucoup de travail)

## Cette version n'est pas encore fonctionnelle

# Importation des modules :
import time as time
import fonction as m
from os import path
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage


# Lancement du jeu avec affichage et prise en compte des reponses
def jeu(reponse,prop):
    global proposition
    prop=prop.upper()
    entr1.delete(0,len(prop))
    if path.exists('score.txt') == False :  # Test de l'existence du fichier 'score.txt'
        m.initDoc()
    mot = m.initMot(reponse)
    chgmMot = m.chgmMot(mot,prop,reponse)
    proposition.append(prop)   # ajout des proposition dans une liste
    labelMot['text'] = 'Mot à trouver : ' + ' '.join(m.chgmMot(mot,prop,reponse))
    labelEssai['text'] = " Nombre d'Essai(s) restant :" + str(8-len(proposition))
    photo['file'] = m.penduImg(8-len(proposition))

proposition=[]
reponse = m.choix()
mot = m.initMot(reponse)

# Partie Graphique

# Fenêtre
fen = Tk()
fen.title("Jeu Du Pendu")

# Canvas avec le .gif
Canevas = Canvas(fen, width = 300, height = 300)
photo = PhotoImage(file = 'bonhomme8.gif')
item = Canevas.create_image(150,150,image = photo)
Canevas.pack()

# Affichage de l'entrée et du mot à chercher
entr1 = Entry(fen)
labelMot = Label(fen, text = "Mot à Trouver : " + ' '.join(m.chgmMot(mot,entr1.get(),reponse)))
labelMot.pack()

# Bouton permettant la soummision d'une réponse
buttonProp = Button(fen, text="Proposition",command = lambda: jeu(reponse,entr1.get()))

entr1.pack()
buttonProp.pack()
# Affiche le nombre d'essai restant 
labelEssai = Label(fen, text = " Nombre d'Essai(s) restant :"+str(8))
labelEssai.pack()

# Bonton permettant de sortir de la fenêtre
buttonQuitt = Button(fen, text="QUITTER", command = fen.destroy)
buttonQuitt.pack()


fen.mainloop()

# cd .\TP_Pendu\Graphique\

