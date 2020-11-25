# Je suis un bout de code python

salut=[]

def crea(liste):
    for i in range(50):
        if i%2==0:
            liste.append(1)
        else:
            liste.append(0)
    return liste

