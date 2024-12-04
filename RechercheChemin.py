from utils import ASSODIRECTIONNOMBRE, accessiblechemins, G

def ReconstruireChemin(depart, arrivee, arcs):
    chemin = [arrivee]
    dicoArcs = dict(arcs)
    #print(f"Arcs: {arcs}")
    #print(f"dicoArcs: {dicoArcs}")

    while chemin[0] != depart:
       chemin.insert(0, dicoArcs[chemin[0]])

    return chemin

def CheminToGo(G, d, a):
    accessibleVerticises, links = accessiblechemins(G, d)
    #print(accessibleVerticises)
    if a not in accessibleVerticises:
        raise Warning("Pas de chemin trouvé.")
    return ReconstruireChemin(d,a, links)

def PrintCreateGPS(graph, chemin:list) -> None:
    #print(f"Graph: {graph}")
    print(f"Depart, vous apparaissez dans le monde, voila comment sortir: ")
    for i in range(len(chemin)-1):
        print(ASSODIRECTIONNOMBRE[dict(graph[chemin[i]][1])[chemin[i+1]]]) # On va chercher la position du prochain noeud dans le graphe, tres neste.
    #print("Sorti !")

def CreateGPS(graph, chemin:list) -> str:
    rep = ""
    rep += f"Depart, vous apparaissez dans le monde, voila comment sortir:"
    for i in range(len(chemin)-1):
        rep += f"\n{ASSODIRECTIONNOMBRE[dict(graph[chemin[i]][1])[chemin[i+1]]]}" # On va chercher la position du prochain noeud dans le graphe, tres neste.
    #print("Sorti !")
    return rep

def test():
    flag = True
    depart = 0
    arrivee = 6
    #print(CheminToGo(G, depart, arrivee))
    #PrintCreateGPS(G, CheminToGo(G, depart, arrivee))
    print(CreateGPS(G, CheminToGo(G, depart, arrivee)))
    flag = flag and CheminToGo(G, depart, arrivee)
    return flag

if __name__ == "__main__":
    assert test()