def multiple13(n):
   '''affiche les n premiers multiples de 13
   n est un entier positif'''
   for i in range(1,n+1):
    print(13*i)

def puissance2(n):
    '''affiche les n premières puissances de 2
    n est une entier positif'''
    for i in range(0,n+1):
        print(2**i)

def sommeentiers(n):
    '''affiche la somme des n premiers entiers
    n est une entier positif
    renvoie un entier'''
    somme=0
    for i in range(1,n+1):
        somme=somme+i
    return somme

def sommediviseurs(n):
    '''calcule la somme des diviseurs de n
    n est une entier positif non nul
    renvoie un entier'''
    somme=0
    for i in range(1,n+1):
        if n%i==0:
            somme=somme+i
    return somme

def nombreparfait(n):
    '''vérifie si un nombre est parfait
    (si il est géal à la moitié de la somme de ses diviseurs)
    n est un entier positif non nul
    renvoie un booléen'''
    if n==sommediviseurs(n)/2:
        return True
    else:
        return False

def premier(n):
    '''vérifie si un nombre est premier
    n est une entier positif supérieur ou égal à 2
    renvoie un booléen'''
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

def lancer6():
    '''détermine au bout de combien de lancers aléatoires on obtient un 6 au dé
    renvoie un entier positif'''
    import random
    s=1
    alea=random.randint(1,6)
    while alea!=6:
        alea=random.randint(1,6)
        s=s+1
    return s


def moyennelancer6(n):
    '''détermne la moyenne de n lancers6
    renvoie un entier'''
    pass
