from utils import DOTPATH, GetGraphInData
from RechercheChemin import accessiblechemins, ReconstruireCheminAsTuples

def CreateLineInDot(gauche,droite,etiquette,listekeysrouge):
    if (gauche, droite) in listekeysrouge:
        text = f'"{gauche}" -> "{droite}" [label = "{etiquette}"] [fontcolor=red] [color=red]'
    else : 
        text = f'"{gauche}" -> "{droite}" [label = "{etiquette}"] [fontcolor=darkgreen]'
    return text 

def CreerCarteVisite(graph,fichier):
    """
    Creer le graphe sur un fichier dot ouvert préalablement
    """
    fichier.write("digraph g{ \n")
    for key in graph:
        fichier.write(f'"{graph[key][0]}";\n')
        for suite in graph[key][1]:
            fichier.write(CreateLineInDot(graph[key][0],graph[suite[0]][0],suite[1],[]))
            fichier.write("\n")
    fichier.write("}")

def CreerCarteAvecChemin(graph,fichier, entree, sortie):
    listarcs=[(graph[k][0], graph[v][0]) for k,v in ReconstruireCheminAsTuples(entree, sortie, accessiblechemins(graph,entree)[1])]
    listechemin = [arc[0] for arc in listarcs]
    fichier.write("digraph g{ \n")
    for key in graph:
        if graph[key][0] in listechemin or key == sortie: # On met En couleur
            fichier.write(f'"{graph[key][0]}" [fontcolor=black] [color=red];\n')
        else :
            fichier.write(f'"{graph[key][0]}";\n')

        for suite in graph[key][1]:
            fichier.write(CreateLineInDot(graph[key][0],graph[suite[0]][0],suite[1],listarcs))
            fichier.write("\n")
    fichier.write("}")

if __name__ == "__main__":
    with open(DOTPATH, "w") as carte:
        g = GetGraphInData("paris")
        CreerCarteAvecChemin(g,carte,0,6)
 
