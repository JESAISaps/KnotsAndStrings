import json

G = { 0: ("Entree", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Salle à manger", [(0, "Sud"), (4, "Est")]),
      2: ("Terrasse", [(5, "Est"), (0, "Ouest")]),
      3: ("Route", [(0, "Nord"), (6, "Est")]),
      4: ("Garde-manger", [(1, "Ouest")]),
      5: ("Jardin.", [(2, "Ouest")]),
      6: ("Sortie", [])}


ASSODIRECTIONNOMBRE = {"Nord":1, "Sud":2, "Est":3, "Ouest":4}

def successeurs(graphe,sommet)-> list[int]:
    liste =[]
    for element in graphe[sommet][1]:
           liste.append(element[0])
    return liste

def accessible(graphe,sommet1):
    reponse=[sommet1]
    sommetvus=successeurs(graphe,sommet1)
    while sommetvus != []:
         voisin=sommetvus.pop()
         if voisin in reponse :
              pass
         else :
              reponse.append(voisin)
              sommetvus += successeurs(graphe,voisin)
    return reponse
  
def accessiblechemins(graphe,sommet1):
    sommetavant=sommet1
    reponse=[sommet1]
    chemins=[]
    sommetvus=successeurs(graphe,sommet1)
    while sommetvus != []:
         voisin=sommetvus.pop()
         if voisin in reponse :
              pass
         else :
              reponse.append(voisin)
              chemins.append([voisin,sommetavant])
              sommetvus += successeurs(graphe,voisin)
              sommetavant=voisin
    return reponse, chemins

########
########
########

"""Exemples de graphes"""

# construit le graphe du 1er exemple du cours
def graphe_cours_exemple1():
    return {"a":["e"],
            "b":["g","c"],
            "c":["g"],
            "d":["a","e"],
            "e":["f"],
            "f":["g"],
            "g":[]}

# Génère un graphe orienté à n sommets
# identifiés par les entiers de [1,n-1],
# et avec un arc de i vers j d'autant plus
# souvent que k est petit.
def graphe_oriente(n, k):
  d = {}
  for i in range(0, n):
    d[i] = list()
    for j in range(0, n):
      if ((i + j)^2) % (i % k + k) == 0 and i != j:
        d[i].append(j)
  return d


# Génère un fichier .dot pour la visualisation
# du graphe avec dotty.
# fichier est supposé ouvert.
def generate_dot(g, fichier):
    fichier.write("digraph G {\n")
    for x in g.keys():
        for y in g[x]:
            fichier.write(str(x)+"->"+str(y)+"\n")
    fichier.write("}\n")


def accessiblechemins(G,d):
    """
    Renvoie l'ensemble des sommets accessibles depuis d
    """
    monde = {d}
    oldVertex = d
    sommetsAccessibles = set(G[d])
    arcs = set()

    while sommetsAccessibles != set():
       nextVertex = sommetsAccessibles.pop()
       monde.add(nextVertex)
       arcs.add((nextVertex, oldVertex))
       oldVertex = nextVertex
       sommetsAccessibles.update([sommet for sommet in G[nextVertex] if sommet not in monde])

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

def test():
    #g1 = graphe_cours_exemple1()
    #f1 = open("testg1.dot","wt")
    #generate_dot(g1,f1)
    #f1.close()
    g2 = graphe_oriente(10,5)
    f2 = open("testg2.dot","wt")
    generate_dot(g2,f2)
    f2.close()
    print(g2)
    print(accessible(g2, 1))
    print(RecontruireChemin(1,2, accessible(g2,1)[1]))


if __name__ == "__main__":
    #with open("data.json", "w") as file:
    #    json.dump(G, file)

    with open("data.json", "r") as file:
        g = json.load(file)
        print(g)