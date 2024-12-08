import json
import os

G = { 0: ("Entree", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Salle a manger", [(0, "Sud"), (4, "Est")]),
      2: ("Terrasse", [(5, "Est"), (0, "Ouest")]),
      3: ("Route", [(0, "Nord"), (6, "Est"), [7, "Ouest"]]),
      4: ("Garde-manger", [(1, "Ouest")]),
      5: ("Jardin", [(2, "Ouest")]),
      6: ("Sortie", []),
      7: ("Trou", [(8, "Nord")]),
      8: ("Perdu", [(7, "Sud")])}


G1 = { 0: ("Bienvenue dans ce monde!", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Vous êtes dans la salle à manger.", [(0, "Sud"), (4, "Est")]),
      2: ("Vous êtes sur la terrasse, sous le préau.", [(5, "Est"), (0, "Ouest")]),
      3: ("Vous êtes sur la route, devant la maison.", [(0, "Nord"), (6, "Est")]),
      4: ("Vous vous trouvez dans le garde-manger.", [(1, "Ouest")]),
      5: ("Vous êtes dans le jardin.", [(2, "Ouest")]),
      6: ("Vous êtes sorti du monde, bravo!", [])}

DIRECTIONS = ["Nord", "Sud", "Est", "Ouest","Nord Ouest","Nord Est","Sud Est","Sud Ouest"]
ASSODIRECTIONNOMBRE = {DIRECTIONS[i-1]:i for i in range(1,len(DIRECTIONS)+1)}
ASSONOMBREDIRECTION = {ASSODIRECTIONNOMBRE[key]:key for key in ASSODIRECTIONNOMBRE}
VIRTUALEXITNUMBER = 314159265359
if os.name == "nt":
    DOTPATH = "KnotsAndStrings/Dots/dot.dot"
    JSONPATH = "KnotsAndStrings/data/data.json"
elif os.name == "posix":
    DOTPATH = "./Dots/dot.dot"
    JSONPATH = "./data/data.json"

def successeurs(graphe,sommet)-> list[int]:
    liste =[]
    for element in graphe[sommet][1]:
           liste.append(element[0])
    return liste

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

    while chemin[0] != depart:
       chemin.insert(0, dicoArcs[chemin[0]])

    return chemin

def IsVertexAccessible(G, d, a):
    accessibleVerticises, links = accessiblechemins(G, d)
    if a not in accessibleVerticises:
       return False, accessibleVerticises
    return True, RecontruireChemin(a,d, links)

def GetAllGraphsInData():
    """
    Returns all graphs in data.json. First list is the list of names
    Keys from inside the graph are converted back to int
    """
    try:
        with open(JSONPATH, "r") as file:
            g = json.load(file, object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()})
        return g
    except json.decoder.JSONDecodeError as er:
        print(f"Erreur: {er}\n data.json potentiellement vide.")
        return {}

def GetGraphInData(graphName:str):
    return GetAllGraphsInData()[graphName]

def SaveGraph(graph, name:str):
    """
    Adds graph graph with name name to json file, overrides
    if name already exits
    """
    with open(JSONPATH, "r") as file:
        g = GetAllGraphsInData()
    with open(JSONPATH, "w") as file:
        g[name] = graph
        json.dump(g, file)

if __name__ == "__main__":
    pass
    #print(GetAllGraphsInData())
    #print(GetGraphInData("G"))
    #SaveGraph(G, "heheheheheheh")