import doctest
import webbrowser
from utils import GetGraphInData, DOTPATH, accessiblecheminsJickstra, accessiblechemins
from CreationCarte import CreerCarteAvecChemin, CreerCarteVisite
from SortieRatee import GetImpossibleExits, GetPossibleExitsByName, GetExits
from BaladeLabyrinthe import visite
from EditeurLabyrinteV2 import StartCreation
from RechercheChemin import PrintCreateGPS
import graphviz


def ShowLabyrinth(graphName:str, start:int=None, end:int=None, useJickstra:bool=False, useCost:bool=False):
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
                CreerCarteAvecChemin(graph, file, start, end, useJickstra, useCost)
            case _:
                raise AttributeError("Il faut donner un depart et une fin, ou rien du tout.")

    graphviz.render("dot", "pdf", DOTPATH)
    
    # Ne marche que sous linux, windows est pas tres pratique faut mettre le chemin absolu
    webbrowser.open(f"{DOTPATH}.pdf", 2)

def CallAccessibles(graphName:str, entree):
    graph = GetGraphInData(graphName)
    print(accessiblechemins(graph, entree))

def CallAccessiblesJidstrka(graphName:str, entree):
    graph = GetGraphInData(graphName)
    print(accessiblecheminsJickstra(graph, entree))

def SortieImpossible(graphName:str):    
    graph = GetGraphInData(graphName)
    print(f"Sortie impossible par les sommets suivants : {GetImpossibleExits(graph)}")

def SortiePossible(graphName:str):
    graph = GetGraphInData(graphName)
    print(f"Sortie possible par les sommet suivants : {GetPossibleExitsByName(graph)}")

def SortiesGraph(graphName:str):
    graph = GetGraphInData(graphName)
    print(f"Les sorties du graph {graphName} sont : {GetExits(graph)}")

def CallVisite(graphName:str, entree:int):
    graph = GetGraphInData(graphName)
    visite(graph, entree)

def CallEditeur():
    StartCreation()

def CallGPS(graphName:str, entree, sortie):
    graph = GetGraphInData(graphName)
    PrintCreateGPS(graph, entree, sortie)

if __name__ == "__main__":
    doctest.testfile("doctest.txt")

    # 1
    #CallVisite("fsf", 1)

    # 2
    #CallAccessibles("fsf", 1)
    #CallAccessiblesJidstrka("fsf", 1)
    
    # 2.1
    #CallGPS("fsf", 1, 37)

    # Pour le piping: 'python RechercheChemin.py pipe g 0 6| python BaladeLabyrinthe.py pipe g 0'
    # /!\ -> Le piping ne fonctionne pas sur les graphs qui ne suivent pas la convention nord-sud ... pour les directions,
    # a cause de gps qui doit aller chercher ce que l'utilisateur doit entrer pour donner un bon gps. Les contextes etants
    # differents, les numeros a saisir sont differents.

    # 3
    #ShowLabyrinth("fsf", 1, 37, True)

    # 4
    #SortieImpossible("fsf")
    #SortiePossible("fsf")
    #SortiesGraph("fsf")

    # ++

    # Editeur
    #CallEditeur()

    # Parler de json
    # Géré en parti les graphs incompatibles
    # Géré la colab avec GIT