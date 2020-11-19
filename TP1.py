# TP n°1

# II - Calendrier
# Fonction testant si une année est bissextile ou pas :
def testBissextile(année):
    if (année % 400 % 4) == 0: # Test année bissextile
        return True
    else :
        return False
# Fonction donnant le nombre de jour dans le mois et l'année demandée :
def nbJour(mois,année):
    jour=0
    if mois in [1,3,5,7,8,10,12]:
        jour=31
    elif mois in [4,6,9,11]:
        jour=30
    else:
        if testBissextile(année)==True:
            jour=29
        else:
            jour=28
    return jour
# Fonction vérifiant la validité d'une date :
def dateValide(jour,mois,année):
    if mois in [1,2,3,4,5,6,7,8,9,10,11,12]:   # test de la validité du mois
        if 0<jour and jour<=nbJour(mois,année):
            return True
        else:
            return False
    else:
        return False
# Saisie d'une date puis vérif de sa validité:
def validite():
    print("Saisissez Votre Date :")
    jour=int(input("Jour : "))
    mois=int(input("Mois : "))
    année=int(input("Année : "))
    if dateValide(jour,mois,année) == True:
        print("Date Valide")
    else:
        print("Date Non Valide")
#Lancement de la fonction
#validite()

# III - Impôt d'un célibataire
# Calcul des impots pour un célibataire en 2019 :
def mesImpots():
    revenu = int(input("Vos Revenus sont de : "))  # Saisi des revenus
    impots = 0
    if 9964 <= revenu and revenu <= 27519:  # Différents test avec calcul des impots
        impots = (revenu - 9964) * (14/100)
    elif 27519 <= revenu and revenu <= 73779:
        impots = ((revenu - 27519) * (30/100)) + ((27519 - 9964) * (14/100))
    elif 73779 <= revenu and revenu <= 156244:
        impots = ((revenu - 73779) * (41/100)) + ((revenu - 27519) * (30/100)) + ((27519 - 9964) * (14/100))
    elif revenu > 156244:
        impots = ((revenu - 156244) * (45/100)) + ((revenu - 73779) * (41/100)) + ((revenu - 27519) * (30/100)) + ((27519 - 9964) * (14/100))
    print("Vos impots seront à hauteur de :",round(impots,2),"€ en 2019")
#Lancement de la fonction :
#mesImpots()

# IV - Multiplication de Matrices

def multiplication(A,B):   # Calcul Matriciel par construction des lignes
    C=[]
    ligne=[]
    if len(A) == len(B) or len(A[0]) == len(B):  # Test de compatibilité
        for i in range(len(A)):  # Déplacement dans les lignes
            for j in range(len(B[0])):  # Déplacement dans les colonnes
                sum = 0
                for k in range(len(A[0])):   # Calcul terme à terme du produit matriciel
                    sum += A[i][k]*B[k][j]   
                ligne.append(sum)  # Création de chacune des lignes en ajoutant les termes précédemment calculés
            C.append(ligne)   # Ajout des lignes à la matrice C = A x B
            ligne=[]   # Réinitialisation de la liste pour calcul d'une nouvelle ligne
        return C
    else: 
        return "Incompatibilité des dimension de matrice"

# V - Récursivité, Tours de Hanoï
nb=0
def hanoi(n,a=1,b=2,c=3):
    global nb  # recherche de la variable global "nb"
    if (n > 0):   # test du nombre de palets 
        hanoi(n-1,a,c,b)
        print ("Déplacer le disque du plot",a,"vers le plot",c)
        hanoi(n-1,b,a,c)
        nb+=1 # incrémentation de 1 pour le décompte du nombre de coup à réaliser
#Fonction donnant les étapes de résolution ainsi que le nombre d'étapes
def resolution(nbpalet):
    hanoi(nbpalet)
    print("Le nombre de déplacement nécessaire est de :",nb)
# Execution de la fonction de résolution de la tour de Hanoï
#resolution(4)

# VI - Conjecture de Syracuse
# Fonction donnant la suite de Syracuse pour un entier donnée N de taille nbterme
nbterme = 1000  # nombre de terme dans la série de Syracuse
def Syracuse(N,nbterme):
    Syracuse=[N]
    for i in range(nbterme):
        if Syracuse[-1] % 2 == 0:
            Syracuse.append(int(Syracuse[-1]/2))
        else:
            Syracuse.append(int(Syracuse[-1]*3+1))
    return Syracuse
# Fonction retournant la valeur maximale de cette liste
def altitudeMax(N):
    return max(Syracuse(N,nbterme))
# Fonction retournant le nombre d'itération avant d'arriver à 1
def tempsVol(N):
    for index,valeur in enumerate(Syracuse(N,nbterme)):  # Parcours de la liste avec les indices & valeur de cette dernière à l'aide d'enumerate
        if valeur == 1 :  
            return index

# Quel nombre entre 1 et n possède le temps de vols le plus long ?
n=1000
def MostVol(n):
    tpsvol = [tempsVol(i) for i in range(1,n+1)] # Création de la liste des temps de vol entre 1 et n (ici n = 1000)
    for index,valeur in enumerate(tpsvol): # Parcours de la liste avec enumerate
        if valeur == max(tpsvol):  # test pour trouver la valeur max
            return index

#print("La valeur, comprise entre 1 et",n,"possédant le temps de vol le plus long est :",MostVol(n))

def MostALt(n):
    Alt = [altitudeMax(i) for i in range(1,n+1)] # Création de la liste des temps de vol entre 1 et n (ici n = 1000)
    for index,valeur in enumerate(Alt): # Parcours de la liste avec enumerate
        if valeur == max(Alt):  # test pour trouver la valeur max
            return index

#print("La valeur, comprise entre 1 et",n,"possédant l'altitude la plus importante est :",MostALt(n))

# VII - Nombres Tricolores
# Fonction retournant un bouléen concernant l'appartenance ou non du nombre n à l'ensemble des nombres bouléens
def tricolore(n):
    nbr = list(str(n**2))
    i=0
    while nbr[i] in ["1","4","9"] and i <= (len(nbr)-2):
        i+=1
    if i == len(nbr)-1:
        return True
    else:
        return False
# Fonction renvoyant tous les nombres tricolores entre 1 et N sous forme d'une liste
def tous_les_tricolores(N):
    return [i for i in range(1,N+1) if tricolore(i) == True]

# VIII - Nombres Amicaux