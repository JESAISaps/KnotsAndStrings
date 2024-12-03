from utils import G

def CreateLignInDot(gauche,droite,etiquette):
    text = f'"{gauche}" -> "{droite}" [label = "{etiquette}"] [fontcolor=brown]'
    return text 

def CreerCarteVisite(graph,fichier):
    """
    Creer le graphe sur un fichier dot ouvert préalablement
    """
    fichier.write("digraph g{ \n")
    for key in graph:
        for suite in graph[key][1]:
            fichier.write(CreateLignInDot(graph[key][0],graph[suite[0]][0],suite[1]))
            fichier.write("\n")
    fichier.write("}")

if __name__ == "__main__":
    with open("dot.dot", "w") as carte:
        CreerCarteVisite(G,carte)
 
