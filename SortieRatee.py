from copy import deepcopy
from utils import accessiblechemins, VIRTUALEXITNUMBER
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
    uniqueExit = VIRTUALEXITNUMBER
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

def GetPossibleExits(graph):
    """
    Returns set of vertex from where we can exit
    """
    newGraph = CreateGraphWithUniqueExit(graph)

    return set.difference(accessiblechemins(MirrorGraph(newGraph), VIRTUALEXITNUMBER)[0], {VIRTUALEXITNUMBER})


def GetImpossibleExits(graph):
    """
    Returns tag of verticies from where we can't escape
    """
    verticies = {key for key in graph}
    return {graph[key][0] for key in set.difference(verticies, GetPossibleExits(graph))}

if __name__ == "__main__":
    print(GetPossibleExits(G))