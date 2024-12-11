import doctest
import json
import webbrowser
from utils import GetGraphInData, DOTPATH
from CreationCarte import CreerCarteAvecChemin, CreerCarteVisite
from SortieRatee import GetImpossibleExits
import graphviz



def ShowLabyrinth(name, start=None, end=None):
    """
    Crée le dot du labyrinthe et l'affiche.
    Si start et end sont donnés, alors on met le chemin en rouge.
    """

    graph = GetGraphInData(name)

    with open(DOTPATH, "w") as file:
        match start,end:
            case None, None:
                CreerCarteVisite(graph, file)
            case int(), int():
                CreerCarteAvecChemin(graph, file, start, end)
            case _:
                raise AttributeError("Il faut donner un depart et une fin, ou rien du tout.")

    graphviz.render("dot", "pdf", DOTPATH)
    
    # Ne marche que sous linux, windows est pas tres pratique faut mettre le chemin absolu
    webbrowser.open(f"{DOTPATH}.pdf", 2)


if __name__ == "__main__":
    doctest.testfile("doctest.txt")
    g = GetGraphInData("g")
    #print(GetImpossibleExits(g))
    ShowLabyrinth("g", 0, 6)