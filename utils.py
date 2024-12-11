import json
import os

G = { 0: ("Entree", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Salle a manger", [(0, "Sud"), (4, "Est")]),
      2: ("Terrasse", [(5, "Est"), (0, "Ouest")]),
      3: ("Route", [(0, "Nord"), (6, "Est"), [7, "Ouest"]]),
      4: ("Garde-manger", [(1, "Ouest")]),
      5: ("Jardin", [(2, "Ouest")]),
      6: ("Sortie", []),
      7: ("Trou", [(8, "Nord")]),
      8: ("Perdu", [(7, "Sud")])}

G1 = { 0: ("Bienvenue dans ce monde!", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Vous êtes dans la salle à manger.", [(0, "Sud"), (4, "Est")]),
      2: ("Vous êtes sur la terrasse, sous le préau.", [(5, "Est"), (0, "Ouest")]),
      3: ("Vous êtes sur la route, devant la maison.", [(0, "Nord"), (6, "Est")]),
      4: ("Vous vous trouvez dans le garde-manger.", [(1, "Ouest")]),
      5: ("Vous êtes dans le jardin.", [(2, "Ouest")]),
      6: ("Vous êtes sorti du monde, bravo!", [])}

DIRECTIONS = ["Nord", "Sud", "Est", "Ouest","Nord Ouest","Nord Est","Sud Est","Sud Ouest"]
ASSODIRECTIONNOMBRE = {DIRECTIONS[i-1]:i for i in range(1,len(DIRECTIONS)+1)}
ASSONOMBREDIRECTION = {ASSODIRECTIONNOMBRE[key]:key for key in ASSODIRECTIONNOMBRE}
VIRTUALEXITNUMBER = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674676788952521385225499546667278239864565961163548862305774564980355936345681743241125150760694794510965960940252288797108931456691368672287489405601015033086179286809208747609178249385890097149096759852613655497818931297848216829989487226588048575640142704775551323796414515237462343645428584447952658678210511413547357395231134271661021359695362314429524849371871101457654035902799344037420073105785390621983874478084784896833214457138687519435064302184531910484810053706146806749192781911979399520614196634287544406437451237181921799983910159195
#PI, lol
#VIRTUALEXITNUMBER = 314159265358979323
if os.name == "nt":
    DOTPATH = "KnotsAndStrings/Dots/dot.dot"
    JSONPATH = "KnotsAndStrings/data/data.json"
elif os.name == "posix":
    DOTPATH = "./Dots/dot.dot"
    JSONPATH = "./data/data.json"

class GrapheInexistant(KeyError):
    pass 

def successeurs(graphe,sommet)-> list[int]:
    liste =[]
    for element in graphe[sommet][1]:
           liste.append(element[0])
    return liste

def accessiblechemins(G,d):
    """
    Renvoie l'ensemble des sommets accessibles depuis d
    """
    monde = {d}
    sommetsAccessibles = {sommet[0] for sommet in G[d][1]}
    arcs = {(sommet[0],d) for sommet in G[d][1]}

    while sommetsAccessibles != set():
        nextVertex = sommetsAccessibles.pop()
        monde.add(nextVertex)
        sommetsAccessibles.update({sommet[0] for sommet in G[nextVertex][1] if sommet[0] not in monde})
        arcs.update({(seenVertex[0], nextVertex) for seenVertex in G[nextVertex][1] if seenVertex[0] not in monde})
    return monde, arcs

def RecontruireChemin(depart, arrivee, arcs):
    chemin = [arrivee]
    dicoArcs = dict(arcs)

    while chemin[0] != depart:
       chemin.insert(0, dicoArcs[chemin[0]])

    return chemin

def IsVertexAccessible(G, d, a):
    accessibleVerticises, links = accessiblechemins(G, d)
    if a not in accessibleVerticises:
       return False, accessibleVerticises
    return True, RecontruireChemin(a,d, links)

def GetAllGraphsInData():
    """
    Returns all graphs in data.json. First list is the list of names
    Keys from inside the graph are converted back to int
    """
    try:
        with open(JSONPATH, "r") as file:
            g = json.load(file, object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()})
        return g
    except json.decoder.JSONDecodeError as er:
        print(f"Warning: {er}\n data.json potentiellement vide.")
        return {}

def GetGraphInData(graphName:str):
    """
    Returns graph with name graphName from data. graphName is lowered
    """
    try:
        return GetAllGraphsInData()[graphName.lower()]
    except KeyError:
        raise GrapheInexistant(f"Labyrinthe non trouvé dans data.json, avez-vous bien orthographié '{graphName}' ?")

def SaveGraph(graph, name:str):
    """
    Adds graph graph with name name to json file, overrides
    if name already exits. Name is lowered.
    """
    with open(JSONPATH, "r") as file:
        g = GetAllGraphsInData()
    with open(JSONPATH, "w") as file:
        g[name.lower()] = graph
        json.dump(g, file)

def ShowGraphsInData():
    """
    Affiche les graphs stockés dans la console, faut peut etre changer les numeros dans les liens et mettre les tags
    """
    graphs = GetAllGraphsInData()
    for graph in graphs:
        print(f"{graph}: ")
        for key in graphs[graph]:
            print(f"    {graphs[graph][key][0]}: {graphs[graph][key][1]}")
        print()

if __name__ == "__main__":
    #print(GetGraphInData("G"))
    SaveGraph(G, "g")
    ShowGraphsInData()