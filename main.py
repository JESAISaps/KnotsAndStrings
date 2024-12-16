import doctest
import json
import webbrowser
from utils import GetGraphInData, DOTPATH
from CreationCarte import CreerCarteAvecChemin, CreerCarteVisite
from SortieRatee import GetImpossibleExits, GetPossibleExits
from RechercheChemin import accessiblechemins
from BaladeLabyrinthe import visite
from EditeurLabyrinteV2 import StartCreation
import graphviz



def ShowLabyrinth(graphName:str, start:int=None, end:int=None):
    """
    Crée le dot du labyrinthe et l'affiche.
    Si start et end sont donnés, alors on met le chemin en rouge.
    """

    graph = GetGraphInData(graphName)

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

def CallAccessibles(graphName:str, entree):
    graph = GetGraphInData(graphName)
    print(accessiblechemins(graph, entree))

def SortieImpossible(graphName:str):    
    graph = GetGraphInData(graphName)
    print(GetImpossibleExits(graph))

def SortiePossible(graphName:str):
    graph = GetGraphInData(graphName)
    print(GetPossibleExits(graph))

def CallVisite(graphName:str, entree:int):
    graph = GetGraphInData(graphName)
    visite(graph, entree)

def CallEditeur():
    StartCreation()


if __name__ == "__main__":
    doctest.testfile("doctest.txt")
    #g = GetGraphInData("g")
    #print(GetImpossibleExits(g))
    
    # 1
    #CallVisite("g", 0)

    # 2
    CallAccessibles("g", 0)

    # Pour le piping: 'python RechercheChemin.py pipe | python BaladeLabyrinthe.py pipe'

    # 3
    #ShowLabyrinth("g", 0, 6)

    # 4
    #SortieImpossible("g")
    #SortiePossible("g")

    # ++

    # Editeur
    #CallEditeur()

    # Jijdlrstra:
    # TODO
