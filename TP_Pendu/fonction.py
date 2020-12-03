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

# Choix d'un mot
def choix():
    fichier = open('dicoPenduTrie.txt','r')
    liste = fichier.readlines()
    liste2=[]
    for i in liste:
        liste2.append(i.strip())  # suppression des '/n'
    return liste2[randint(0,len(liste2))]


# Affichage du mot
def affichageMot(mot):
    print('\n')
    for i in mot:
        print(i,end=' ')   # affichage en ligne des éléments de la liste
    print('\n')