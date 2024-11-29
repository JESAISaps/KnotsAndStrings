from BaladeLabyrinthe import creerDicoLiens, ASSODIRECTIONNOMBRE

G:dict = { 0: ("Bienvenue dans ce monde!", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
               1: ("Vous êtes dans la salle à manger.", [(0, "Sud"), (4, "Est")]),
               2: ("Vous êtes sur la terrasse, sous le préau.", [(5, "Est"), (0, "Ouest")]),
               3: ("Vous êtes sur la route, devant la maison.", [(0, "Nord"), (6, "Est")]),
               4: ("Vous vous trouvez dans le garde-manger.", [(1, "Ouest")]),
               5: ("Vous êtes dans le jardin.", [(2, "Ouest")]),
               6: ("Vous êtes sorti du monde, bravo!", [])}

def accessiblechemins(G,d):
    """
    Renvoie l'ensemble des sommets accessibles depuis d
    """
    monde = {d}
    sommetsAccessibles = {sommet[0] for sommet in G[d][1]}
    arcs = {(sommet[0],d) for sommet in G[d][1]}

    while sommetsAccessibles != set():
        nextVertex = sommetsAccessibles.pop()
        monde.add(nextVertex)
        sommetsAccessibles.update({sommet[0] for sommet in G[nextVertex][1] if sommet[0] not in monde})
        arcs.update({(seenVertex[0], nextVertex) for seenVertex in G[nextVertex][1] if seenVertex[0] not in monde})
    return monde, arcs

def RecontruireChemin(depart, arrivee, arcs):
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
    return RecontruireChemin(d,a, links)

def PrintCreateGPS(graph, chemin:list):
    #print(f"Graph: {graph}")
    print(f"Depart, vous apparaissez dans le monde, voila comment sortir: ")
    for i in range(len(chemin)-1):
        print(ASSODIRECTIONNOMBRE[dict(graph[chemin[i]][1])[chemin[i+1]]]) # On va chercher la position du prochain noeud dans le graphe, tres neste.
    #print("Sorti !")

def test():
    flag = True
    depart = 0
    arrivee = 6
    #print(CheminToGo(G, depart, arrivee))
    PrintCreateGPS(G, CheminToGo(G, depart, arrivee))
    flag = flag and CheminToGo(G, depart, arrivee)
    return flag

def TestAccessiblesChemins():
    
    print(accessiblechemins(G,0))

if __name__ == "__main__":
    assert test()
    #TestAccessiblesChemins()