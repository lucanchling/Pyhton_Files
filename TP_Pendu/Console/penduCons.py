# Header
# Pendu version Console
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files/tree/main/TP_Pendu
# 3 Décembre 2020
# To Do : 


# Importation des modules :
import time as time
import fonction as m
from os import path

# Lancement du jeu avec affichage et prise en compte des reponses
def jeu(reponse):
    if path.exists('score.txt') == False :  # Test de l'existence du fichier 'score.txt'
        m.initDoc()
    mot,proposition,c,prop = m.initMot(reponse),[],0,''
    print("Le record actuel est de :",m.record(),"pts")
    print("Le mot à trouver est le suivant :")
    m.affichageMot(mot)  # Premier affichage
    tic = time.time()  # début du chrono
    while (prop != reponse) and (c < 8):  
        prop = input(str("Proposition de lettre ou de mot : ")).upper()  # Mise en majucule
        if prop in proposition:
            print("Vous l'avez déjà proposé !")
        proposition.append(prop)   # ajout des proposition dans une liste
        m.affichageMot(m.chgmMot(mot,prop,reponse))  # affichage du mot actualisé
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
        print("C'est perdu, le mot était :",reponse)
    else :
        partie = True
        print("C'est gagné, vous avez mis",c,"essais !")
    print(m.score(partie,tps,c))
    rejouer = input(str("Voulez-Vous rejouez ? (O/N) ")).upper()
    if rejouer == "O":
        jeu(m.choixMot())

# Lancement de la première partie
jeu(m.choixMot())


