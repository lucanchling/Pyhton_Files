# Header
# Pendu version Graphique
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files
# 10 Décembre 2020
# To Do : 


# Importation des modules :
import time as time
import fonction as m
from os import path
from tkinter import Tk, Button, Label, Entry

# Lancement du jeu avec affichage et prise en compte des réponses
def jeu(réponse):
    if path.exists('score.txt') == False :  # Test de l'existence du fichier 'score.txt'
        m.initDoc()
    mot,proposition,c,prop = m.initMot(réponse),[],0,''
    print("Le record actuel est de :",m.record(),"pts")
    print("Le mot à trouver est le suivant :")
    m.affichageMot(mot)  # Premier affichage
    tic = time.time()  # début du chrono
    while (prop != réponse) and (c < 8):  
        prop = input(str("Proposition de lettre ou de mot : ")).upper()  # Mise en majucule
        if prop in proposition:
            print("Vous l'avez déjà proposé !")
        proposition.append(prop)   # ajout des proposition dans une liste
        m.affichageMot(m.chgmMot(mot,prop,réponse))  # affichage du mot actualisé
        print("Vous avez déjà proposé : ")
        for i in proposition:
            print(i,end=", ")
        print('\n')
        print("Il vous reste",8-(c+1),"chances !")
        c+=1
    tac = time.time()  # fin du chrono
    tps = round(tac - tic,2)  # calcul de la durée
    if c==8:
        partie = False
        print("C'est perdu, le mot était :",réponse)
    else :
        partie = True
        print("C'est gagné, vous avez mis",c,"essais !")
    print(m.score(partie,tps,c))
    rejouer = input(str("Voulez-Vous rejouez ? (O/N) ")).upper()
    if rejouer == "O":
        jeu(m.choixMot())



# Partie Graphique
fen = Tk()
labelMot = Label(fen, text = "Salut")
labelMot.pack()