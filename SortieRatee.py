from copy import deepcopy
from RechercheChemin import accessiblechemins
from utils import G

def GetExits(graph):
    return {key for key in graph if graph[key][1] == []}

def CreateGraphWithUniqueExit(originGraph):
    """
    Returns new graph with unique exit called -1, and without tags
    """
    graph = deepcopy(originGraph)
    exits:set = GetExits(graph)
    uniqueExit = -1
    for exit in exits:
        assert graph[exit][1] == []
        graph[exit][1].append((uniqueExit, "To Virtual Exit"))
    graph[uniqueExit] = ("Virtual Exit", [])
    return graph

def MirrorGraph(originGraph):
    """
    Returns mirrored graph
    """
    graph = {key:(None, []) for key in originGraph}

    for key in originGraph:
        for vertex, _ in originGraph[key][1]:
            graph[vertex][1].append((key, None))
    
    return graph

def GetPossibleExit(graph):
    """
    Returns set of vertex from where we can exit
    """
    newGraph = CreateGraphWithUniqueExit(graph)
    print(newGraph)

    return accessiblechemins(MirrorGraph(CreateGraphWithUniqueExit(graph)), -1)[0]

if __name__ == "__main__":
    print(GetPossibleExit(G))