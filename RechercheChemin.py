from utils import ASSODIRECTIONNOMBRE, accessiblechemins, G, accessiblecheminsJickstra, ASSONOMBREDIRECTION, GetGraphInData
from sys import argv

isPiping = False
if len(argv) > 1 and argv[1] == "pipe":
    isPiping = True

def ReconstruireChemin(depart, arrivee, arcs):
    """
    Retourne le chemin de depart a arrivee sous la forme de succession de sommets
    """
    chemin = [arrivee]
    dicoArcs = dict(arcs)
    #print(f"Arcs: {arcs}")
    #print(f"dicoArcs: {dicoArcs}")

    while chemin[0] != depart:
       chemin.insert(0, dicoArcs[chemin[0]])

    return chemin

def ReconstruireCheminAsTuples(depart, arrivee, arcs) -> list[tuple[int, int]]:
    """
    Retourne le chemin de depart a arrivée sous la formes d'arcs. (enleve les arcs inutiles)
    arcs de la forme [(sommet : provenance)]
    """
    dico = dict(arcs)
    rep = [(dico[arrivee], arrivee)]

    while rep[0][0] != depart:
        rep.insert(0,(dico[rep[0][0]], rep[0][0]))
    return rep

def CheminToGo(G, d, a):
    """
    Retourne la liste des cles des sommets du graph G pour aller du sommet d au sommet a
    """
    accessibleVerticises, links = accessiblecheminsJickstra(G, d)
    #print(accessibleVerticises)
    if a not in accessibleVerticises:
        raise Warning("Pas de chemin trouvé.")
    return ReconstruireChemin(d,a, links)

def PrintCreateGPS(graph, depart, arrivee) -> None:
    #print(f"Graph: {graph}")
    chemin = CheminToGo(graph, depart, arrivee)
    print(f"Depart, vous apparaissez dans le monde, voila comment sortir: ")
    startingIndex = 0
    try:
        graph[0]
    except KeyError:
        startingIndex = 1
    for i in range(startingIndex, len(chemin)-1):
        element = dict(graph[chemin[i]][1])[chemin[i+1]]
        
        # Pas parfait mais fais le taf pour les graphs incompatibles.
        if element not in ASSODIRECTIONNOMBRE.keys():        
            newValueIndex = max(ASSONOMBREDIRECTION.keys()) +1        
            ASSODIRECTIONNOMBRE[element] = newValueIndex        
            ASSONOMBREDIRECTION[newValueIndex] = element
            
        print(ASSODIRECTIONNOMBRE[element]) # On va chercher la position du prochain noeud dans le graphe, tres neste.
    print("Sorti !")

def CreateGPS(graph, chemin:list) -> str:
    rep = ""
    rep += f"Depart, vous apparaissez dans le monde, voila comment sortir:"
    for i in range(len(chemin)-1):
        rep += f"\n{ASSODIRECTIONNOMBRE[dict(graph[chemin[i]][1])[chemin[i+1]]]}" # On va chercher la position du prochain noeud dans le graphe, tres neste.
    return rep



def test():
    flag = True
    depart = 0
    arrivee = 6
    #print(CheminToGo(G, depart, arrivee))
    #PrintCreateGPS(G, CheminToGo(G, depart, arrivee))
    #print(CreateGPS(G, CheminToGo(G, depart, arrivee)))
    flag = flag and CheminToGo(G, depart, arrivee)
    return flag

def StartWithPipe():
    PrintCreateGPS(GetGraphInData(argv[2]), int(argv[3]), int(argv[4]))

if __name__ == "__main__":
    assert test()
    if isPiping:
        StartWithPipe()