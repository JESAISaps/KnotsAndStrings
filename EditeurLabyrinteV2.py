G = { 0: ("Entree", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Salle a manger", [(0, "Sud"), (4, "Est")]),
      2: ("Terrasse", [(5, "Est"), (0, "Ouest")]),
      3: ("Route", [(0, "Nord"), (6, "Est"), [7, "Ouest"]]),
      4: ("Garde-manger", [(1, "Ouest")]),
      5: ("Jardin", [(2, "Ouest")]),
      6: ("Sortie", []),
      7: ("Trou", [(8, "Nord")]),
      8: ("Perdu", [(7, "Sud")])}

from utils import ASSODIRECTIONNOMBRE

def creationLabyrinte():
    G={}
    nombreSommets=getNombreSommets()

def getNombreSommets():
    reponse=""
    while reponse.isdigit()==False or reponse<1:
        reponse=int(input("Combien de sommet dans le graphe?"))

def getListeNomSommets(nombresommets):
    liste=[]
    for sommet in range(nombresommets):
        liste.append(input(f'Quels est le nom du sommet {sommet}'))
    return liste

        
def getAccessiblesEtDirectionDepuisSommet(sommet,listeNomsSommets,dicoAsso):
    listeAcces=[]
    for sommet in listeNomsSommets:
        while acces not in listeNomsSommets :
            acces=input(f'Quels sommet accessibles depuis {sommet}?')
        while direction not in (dicoAsso.values()):
            direction=input(f'Par quelle direction ? {getAssoBellesDirections(dicoAsso)}')
        direction =int(direction)
        listeAcces.append(sommet,direction)
    return sommet,direction

#faire dicoinversé pour récup les étiquettes 

def getAssoBellesDirections(dicoAsso):
    direction=""
    for key in dicoAsso:
        direction+=f'{dicoAsso[key]} : {key}\n'
                                
    return direction 








def test_belledirection(dicoAsso):
    print(fonctionBellesDirections(dicoAsso))
