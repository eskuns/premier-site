# Créé par enzom, le 11/01/2021 en Python 3.7

listehexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
listebinaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

def decbin(n):
    if n > 1:
        decbin(n // 2)
    print(n % 2, end='')
nbr = int(input("Entrez un nombre decimal: "))
decbin(nbr)

def bindec(n):
    if n<10:
        return n
    else:
        return 2*bindec(n/10)+n%2

'''l'une des fonctions donne un résultat plus précis que l'autre,
néamoins il est bien plus complexe'''

def bindec2(string):
    x=len(string)-1
    n=0
    res=0
    while x!=-1:
        if string[x]=="1":
            res=res+2**n
        n=n+1
        x=x-1
    return res

def binhexa(string):
    liste=[]
    res=""
    while len(string)>4:
        liste=liste+[string[-4:]]
        string=string[:-4]
    liste=liste+[string]
    while len(liste[-1])!=4:
        liste[-1]="0"+liste[-1]
    for x in range(len(liste)):
        i=listebinaire.index(liste[x])
        liste[x]=listehexa[i]
    while liste!=[]:
        res=res+liste[-1]
        liste=liste[:-1]
    return res

def hexabin(string):
    res=""
    for x in range(len(string)):
        i=listehexa.index(string[x])
        res=res+listebinaire[i]
    return res

def dechexa(string):
    return binhexa(decbin(string))

def hexadec(string):
    return bindec(hexabin(string))

def hexadec2(string):
    return bindec2(hexabin(string))

