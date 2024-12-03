from copy import deepcopy
from utils import accessiblechemins
if __name__ == "__main__":
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

    return accessiblechemins(MirrorGraph(CreateGraphWithUniqueExit(graph)), -1)[0]

def GetImpossibleExits(graph):
    """
    Returns tag of verticies from where we can't escape
    """
    verticies = {key for key in graph}
    return {graph[key][0] for key in set.difference(verticies, GetPossibleExit(graph))}

if __name__ == "__main__":
    print(GetImpossibleExits(G))