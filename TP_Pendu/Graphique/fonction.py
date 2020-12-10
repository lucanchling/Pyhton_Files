# Header
# Programme regroupant les fonctions utilisées pour le pendu
# Luc Anchling
# github : https://github.com/lucanchling/Pyhton_Files
# 3 Décembre 2020
# To Do :

# Importation des modules :
from random import randint

# Trie la liste des mots pour le pendu
def tri():
    fichier = open('dicoPendu.txt','r')
    liste = fichier.readlines()
    liste2 = []
    liste.sort()   # Tri alphabétique
    for i in range(20): # Taile du mot
        for j in liste:  # Éléments du dictionnaire non trié
            if len(j) == i:   # Tri par taille
                liste2.append(j)
    trie = open('dicoPenduTrie.txt','w')
    trie.writelines(liste2)  #Écriture de la liste triée dans le nouveau fichier
    fichier.close()
    trie.close()

# Choix d'un mot dans la liste triée
def choix():
    fichier = open('dicoPenduTrie.txt','r')
    liste = fichier.readlines()
    liste2=[]
    for i in liste:
        liste2.append(i.strip())  # suppression des '/n'
    return liste2[randint(0,len(liste2))]


# Affichage du mot avec des espaces entre les lettres
def affichageMot(mot):
    for i in mot:
        print(i,end=' ')   # affichage en ligne des éléments de la liste
    print('\n')

# Tri + Choix du mot
def choixMot():
    tri()
    return choix()

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

# Fonction initialisant le document contenant les scores avec un record par défaut à 10000 pts
def initDoc():
    doc = open('score.txt','w')
    doc.write("10000\n")
    doc.close()

# Fonction attribuant à la partie un score tout en actualisant un fichier contenant tous les scores
def score(partie,duree,nbEssai):
    if partie == False :
        return 0
    else:
        score = int(1000000/(nbEssai*duree))
    doc = open('score.txt','a')
    doc.write('\n'+str(score))
    doc.close()
    return score

# Fonction affichant le record actuel
def record():
    doc = open('score.txt','r')
    lscore = doc.readlines()
    doc.close()
    return max(lscore).strip()
