# Header
# Pendu version Console
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files
# 3 Décembre 2020
# To Do :

# Importation des modules :
import time
import fonction as m

# Initialisation du mot à chercher
réponse = m.choix()

# Tri + Choix du mot
def choixMot():
    m.tri()
    return m.choix()

# Initialisation du mot à afficher !
def initMot():
    mot = réponse
    mot1 = [mot[0]]   # affectation de la premiere lettre à la nouvelle liste
    for i in range(1,len(mot)):  # remplacement des autres lettre par des underscores
        mot1.append('_')
    return mot1

# Fonction changeant le mot suivant la proposition faite par l'utilisateur
def chgmMot(mot,prop):
    if prop in réponse:   # test d'appartenance de la proposition dans la réponse
        indices = []
        for indice,valeur in enumerate(réponse): # recherche des indices correspondant à la position de la proposition dans la réponse
            if prop == valeur:  # test
                indices.append(indice)
        for i in indices:
            mot[i] = prop  # Remplacement des '_' par la proposition
        return mot
    else : 
        return mot

    


# Lancement du jeu avec affichage et prise en compte des réponses
def jeu():
    mot = initMot()
    print("Le mot à trouver est le suivant :")
    m.affichageMot(mot)  # Premier affichage
    c = 0
    prop = ''
    while (prop != réponse) and (c < 8):  
        prop = input(str("Proposition de lettre ou de mot : ")).upper()  # Mise en majucule                   
        m.affichageMot(chgmMot(mot,prop))  # affichage du mot actualisé 
        c+=1
    if c==8:
        print("C'est perdu, le mot était :",réponse)
    else :
        print("C'est gagné, vous avez mis",c,"essais !")
        

jeu()
    