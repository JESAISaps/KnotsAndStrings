from utils import ASSODIRECTIONNOMBRE,ASSONOMBREDIRECTION, SaveGraph

def creationLabyrinte(dicoAsso,dicoAssoInverse):
    """
    Renvoie un graphe et son nom (tuple)
    """
    Gini={}
    G={}
    name = getNameGraph()
    nombreSommets=getNombreSommets()
    listeSommets=getListeNomSommets(nombreSommets)

    for i in range(nombreSommets):
        Gini[i]=(listeSommets[i],[])
    DicoInverse=dicoInverse(Gini)

    for i in range(nombreSommets):
        nombreaccessibles=getNombreSommetAccessibles(listeSommets[i],listeSommets,dicoAsso)
        accessibles=getAccessiblesEtDirectionDepuisSommet(listeSommets[i],nombreaccessibles,listeSommets,dicoAsso,dicoAssoInverse)
        for j in range(len(accessibles)):
            numeroSommet=DicoInverse[accessibles[j][0]]
            accessibles[j] = (numeroSommet,accessibles[j][1])
        G[i]=(listeSommets[i], accessibles)
    return G,name

def dicoInverse(dico):
    """
    Renvoie un nouveau dictionnaire qui inverse le numero et le nom
    """

    ginverse={}
    for key in dico.keys():
        ginverse[dico[key][0]]=key
    return ginverse

def getNombreSommets():
    reponse=""
    while not reponse.isdigit() or int(reponse)<1:
        reponse=input("Combien de sommet dans le graphe?")
    return int(reponse)

def getListeNomSommets(nombresommets):
    liste=[]
    for sommet in range(nombresommets):
        liste.append(input(f'Quels est le nom du sommet {sommet} ?\n'))
    return liste


def getNombreSommetAccessibles(sommet,listeSommets,dicoAsso):
    reponse=""
    while not reponse.isdigit() or int(reponse) > len(listeSommets) or int(reponse)>len(dicoAsso):
        reponse = input(f'Combien de sommets accessibles depuis {sommet}? \n')
    return int(reponse)


def beaurappel(listeexistants):
    rappel=""
    for element in listeexistants:
        rappel+=f'{element};'
    return rappel

def getAccessiblesEtDirectionDepuisSommet(sommet,nombreSommetAccessibles,listeNomsSommets,dicoAsso, dicoAssoInverse):
    """
    Renvoie la liste [("sommetAccessible,"direction")]
    """
    listeAcces=[]
    acces=""
    direction = ""
    directionutilisee=[]
    for _ in range(nombreSommetAccessibles):
        while acces not in listeNomsSommets :
            print(f'Rappels sommets existants : {beaurappel(listeNomsSommets)}')
            acces=input(f'Quel sommet accessibles depuis {sommet}?')
        while not direction.isdigit() or int(direction) not in dicoAsso.values() or direction.lower() in directionutilisee:
            direction=input(f'Par quelle direction ? \n{getAssoBellesDirections(dicoAsso)}')
        directionutilisee.append(direction)
        listeAcces.append((acces,dicoAssoInverse[int(direction)]))
        direction = ""
        acces = ""
    return listeAcces

def getAssoBellesDirections(dicoAssonombredirection):
    """
    dicoAsso de la forme {1:"Nord"}
    """
    direction=""
    for key in dicoAssonombredirection:
        direction+=f'{dicoAssonombredirection[key]} : {key}\n'                                
    return direction 

def getNameGraph():
    name=input("Quel est le nom du graphe?\n")
    return name


def test(dicoAsso,sommet,nombreSommetaccessibles,listeNomsSommets,dicoAssoInverse):
    
    """ Test des fonctions écriture et fonction accessible et direction depuis sommet 
    qui es la plus importante pour l'éditeur """
    
    print(getAssoBellesDirections(dicoAsso))
    print(getAccessiblesEtDirectionDepuisSommet(sommet,nombreSommetaccessibles,listeNomsSommets,dicoAsso, dicoAssoInverse))


if __name__ == "__main__":
    grapheetnom=creationLabyrinte(ASSODIRECTIONNOMBRE,ASSONOMBREDIRECTION)
    SaveGraph(grapheetnom[0],grapheetnom[1])
