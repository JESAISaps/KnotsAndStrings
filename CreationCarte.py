from utils import DOTPATH, GetGraphInData, accessiblechemins, accessiblecheminsJickstra
from RechercheChemin import ReconstruireCheminAsTuples

def CreateLineInDot(gauche,droite,etiquette,listekeysrouge):
    if (gauche, droite) in listekeysrouge:
        text = f'"{gauche}" -> "{droite}" [label = "{etiquette}"] [fontcolor=red] [color=red];'
    else : 
        text = f'"{gauche}" -> "{droite}" [label = "{etiquette}"] [fontcolor=darkgreen];'
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

def CreerCarteAvecChemin(graph,fichier, entree:int, sortie:int, useJickstra:bool=False, useCost:bool=False):
    """
    Ecrit dans le fichier en arg le dot du graph.\n
    Tous les arguments suivants sont optionels, mais on ne peut pas en donner un sans donner ceux d'avant.\n
    'entree' et 'sorties' sont utilisé si on veut tracer un chemin en rouge.\n
    useJickstra est utilisé si on veut calculer le chemin a l'aide de Jickstra,\n
    et useCost si on a specifié les couts des chemins dans le graph.
    """

    listarcs=[(graph[k][0], graph[v][0]) for k,v in ReconstruireCheminAsTuples (
        entree, sortie, 
        accessiblecheminsJickstra(graph,entree, useCost)[1] if useJickstra else accessiblechemins(graph, entree)[1]
        )
        ]
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
        g = GetGraphInData("p")
        CreerCarteAvecChemin(g,carte,0,6)
 
