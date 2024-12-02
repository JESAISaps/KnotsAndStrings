from utils import successeurs
from GrapheExamples import G 

def CreerCarteVisite(graph,fichier):
    """
    Creer le graphe sur un fichier dot ouvert préalablement
    """
    fichier.write("digraph g{ \n")
    for key in graph:
        for suite in graph[key][1]:
            fichier.write('"'+str(graph[key][0])+'"' + "->" + '"'+str(graph[suite[0]][0])+'"'+"[label = " +'"'+ str(suite[1])+'"'+"]")
            fichier.write("\n")

    fichier.write("}")

if __name__ == "__main__":
    with open("dot.dot", "w") as carte:
        CreerCarteVisite(G,carte)
 
