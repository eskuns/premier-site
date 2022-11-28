# Créé par LM CONSTRUCTIONS, le 15/12/2020 en Python 3.7
mat= [ [1,2,3],[4,5,6],[7,8,9]]
m= [ [1, 3, 4],[5, 6, 8],[7, 8, 15]]

mat= [ [1,2,3],[4,5,6],[7,8,9]]
for i in mat:
    for j in i:
        print(j)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j])

notes=[[1,7,4,0,4],
    [3,2,0,3,3],
    [4,8,8,4,5],
    [7,1,6,4,3],
    [7,8,2,2,6],
    [2,3,8,5,2],
    [1,10,8,10,5],
    [5,1,1,0,0],
    [8,8,2,2,0]]
def minnotes():
    mini=notes[0][0]
    for i in notes: #Parcours les lignes(élèves)
        for j in i: #Parcours les colonnes(notes)
            if j<mini:
                mini=j
    return(mini)

print(minnotes())

def maxnote(col):
    max=notes[0][0]
    for i in notes:
        j = i[col]
        if j>max:
            max=j
    return(max)

archibald=[3,7,5,8,5]
christobald=[3,7,9]

def moy(liste):
    moyenne=0
    for note in liste:
        moyenne=moyenne+note
    return(moyenne/len(liste))

notes=[[1,7,4,0,4],
    [3,2,0,3,3],
    [4,8,8,4,5],
    [7,1,6,4,3],
    [7,8,2,2,6],
    [2,3,8,5,2],
    [1,10,8,10,5],
    [5,1,1,0,0],
    [8,8,2,2,0]]

def moyparEleve(matrice):
    tabmoy=[]
    for eleve in matrice:#pour chaque élève
        moyenne=moy(eleve)#calcul de la moyenne
        tabmoy.append(moyenne)#ajout dans le tab des moyennes
    return tabmoy

def moyparEleveBis(matrice):
    tabmoy=[]
    for eleve in matrice:
        moyenne=0
        for note in eleve:
            moyenne=moyenne+note
        tabmoy.append(moyenne/len(eleve))
    return tabmoy

def moypareval(matrice):
    moyeval=[0 for i in range(len(matrice[0]))]
    for eleve in matrice:
        moyenne=0
        for i in range(len(eleve)):
            moyeval[i]=moyeval[i]+eleve[i]
    for j in range(len(moyeval)):
        moyeval[j]=moyeval[j]/len(notes)
    return moyeval

def ligne(x,i):
    if x in sudoku[i]:
        return False
    return True

def colonne(x,c):
    sudoku
    for i in range(9):
        if sudoku[i][c]==x:
            return False
    return True

sudoku=[[0,0,3,0,0,4,0,0,8],
    [0,0,5,0,6,0,0,0,1],
    [4,2,0,0,0,7,0,0,0],
    [0,0,0,0,0,0,4,0,0],
    [8,0,0,0,0,5,0,0,3],
    [5,0,0,3,0,6,9,0,7],
    [0,0,6,1,0,0,3,0,0],
    [9,8,0,0,0,0,7,0,0],
    [1,0,0,0,0,0,0,6,0]]