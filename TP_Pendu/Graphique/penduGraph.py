# Header
# Pendu version Graphique
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files/tree/main/TP_Pendu
# 10 Décembre 2020
# To Do :


# Importation des modules :
import time as time
import fonction as m
from os import path
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage, StringVar, messagebox

# Lancement du jeu avec affichage et prise en compte des reponses
def jeu(reponse,prop):
    global proposition
    global mot
    prop=prop.upper()   # Mise en majuscule de la proposition
    entr1.delete(0,len(prop))   # Suppression de la zone de saisie au moment de la soumission de cette dernière
    chgmMot = m.chgmMot(mot,prop,reponse)  # Mise à jour du mot selon la proposition de l'utilisateur
    mot=chgmMot
    if prop not in reponse or prop not in proposition and prop!="":
        proposition.append(prop)  # ajout des propositions dans une liste
    # Mise à jour des informations à afficher
    if len(proposition) <= 7:
        labelMot['text'] = 'Mot à trouver : ' + ' '.join(m.chgmMot(mot,prop,reponse))
        labelEssai['text'] = " Nombre d'Essai(s) restant :" + str(8-len(proposition))
        labelProp['text'] = "Vous avez déjà proposé : "+', '.join(proposition)
        photo['file'] = m.penduImg(8-len(proposition))
    # Lorsque la partie se termine
    if len(proposition) == 8 or prop == reponse:
        if len(proposition) == 8:
            partie = False
        else :
            partie = True
        fen.destroy()  # Fermeture de la fenetre 
        tac=time.time()  # Fin du chrono
        fene = Tk() # Affichage du score dans une autre fenêtre
        fene.title('Résultat')
        labelScore = Label(fene, text = "Votre score est de "+ str(m.score(partie,tac-tic,len(proposition))))
        labelScore.pack()
        fene.mainloop()

# Initialisation de la liste contenant les propositions de l'user, du mot à trouver et du premier affichage à effectuer
proposition=[]
reponse = m.choix()
mot = m.initMot(reponse)
# Initialisation du document des score si il n'existe pas
if path.exists('score.txt') == False :  # Test de l'existence du fichier 'score.txt'
    m.initDoc()
# Déclenchement du chronomètre
tic=time.time()
# Partie Graphique

# Création de la Fenêtre
fen = Tk()
fen.title("Jeu Du Pendu")

# Canvas avec le .gif
Canevas = Canvas(fen, width = 300, height = 300)
photo = PhotoImage(file = 'bonhomme8.gif')
item = Canevas.create_image(150,150,image = photo)
Canevas.pack()

# Création de l'objet entry (permettant à l'utilisateur de saisir une réponse)
entr1 = Entry(fen)

# Affichage du mot à chercher
labelMot = Label(fen, text = "Mot à Trouver : " + ' '.join(m.chgmMot(mot,entr1.get(),reponse)))
labelMot.pack()

# AFfichage du record
labelRecord = Label(fen, text = "Le Record est de : " + str(m.record()) + "pts")
labelRecord.pack()
# Bouton permettant la soummision d'une réponse
buttonProp = Button(fen, text="Proposition",command = lambda: jeu(reponse,entr1.get()))
# Zone de saisie de l'entrée utilisateur
entr1.pack()
buttonProp.pack()
# Affiche le nombre d'essai restant 
labelEssai = Label(fen, text = " Nombre d'Essai(s) restant :"+str(8))
labelEssai.pack()
# Label permettant l'affichage de spropositions déjà faites par l'utilisateur
labelProp = Label(fen)
labelProp.pack()
# Bonton permettant de sortir de la fenêtre
buttonQuitt = Button(fen, text="QUITTER", command = fen.destroy)
buttonQuitt.pack()

fen.mainloop()

# cd .\TP_Pendu\Graphique\
