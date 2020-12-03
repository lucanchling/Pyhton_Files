# Header
# Pendu version Console
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files
# 3 Décembre 2020
# To Do : Gérer le score et l'historique des score ; séparer un max de fonction pour la version Tkinter

# Importation des modules :
import time as time
import json
import fonction as m


# Tri + Choix du mot
def choixMot():
    m.tri()
    return m.choix()


# Initialisation du mot à afficher !
def initMot(réponse):
    mot = réponse
    mot1 = [mot[0]]   # affectation de la premiere lettre à la nouvelle liste
    for i in range(1,len(mot)):  # remplacement des autres lettre par des underscores
        mot1.append('_')
    return mot1

# Fonction changeant le mot suivant la proposition faite par l'utilisateur
def chgmMot(mot,prop,réponse):
    if prop in réponse:   # test d'appartenance de la proposition dans la réponse
        indices = []
        for indice,valeur in enumerate(réponse): # recherche des indices correspondant à la position de la proposition dans la réponse
            if prop == valeur:  # test
                indices.append(indice) # ajout des indices correspondant aux emplacements dans la réponse
        for i in indices:
            mot[i] = prop  # Remplacement des '_' par la proposition
        return mot
    else : 
        return mot


# Lancement du jeu avec affichage et prise en compte des réponses
def jeu(réponse):
    mot = initMot(réponse)
    proposition = []
    print("Le mot à trouver est le suivant :")
    m.affichageMot(mot)  # Premier affichage
    global c
    c=0
    prop = ''
    global tps
    global partie
    tic = time.time()  # début du chrono
    while (prop != réponse) and (c < 8):  
        prop = input(str("Proposition de lettre ou de mot : ")).upper()  # Mise en majucule
        if prop in proposition:
            print("Vous l'avez déjà proposé !")
        proposition.append(prop)   # ajout des proposition dans une liste
        m.affichageMot(chgmMot(mot,prop,réponse))  # affichage du mot actualisé
        print("Vous avez déjà proposé : ")
        for i in proposition:
            print(i,end=", ")
        print('\n')
        print("Il vous reste",8-(c+1),"chances !")
        c+=1
        print(c)
    tac = time.time()  # fin du chrono
    tps = round(tac - tic,2)  # calcul de la durée
    if c==8:
        partie = False
        print("C'est perdu, le mot était :",réponse)
    else :
        partie = True
        print("C'est gagné, vous avez mis",c,"essais !")
    rejouer = input(str("Voulez-Vous rejouez ? (O/N) ")).upper()
    if rejouer == "O":
        jeu(choixMot())

# Lancement de la première partie
jeu(choixMot())


def score():
    nbEssai = c
    if partie == False :
        return 0
    else:
        return int(1000000/(nbEssai*tps))

print("Votre score est de :",score())
