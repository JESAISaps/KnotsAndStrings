import json
import os
from dataclasses import dataclass
from queue import PriorityQueue


G = { 0: ("Entree", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Salle a manger", [(0, "Sud"), (4, "Est")]),
      2: ("Terrasse", [(5, "Est"), (0, "Ouest")]),
      3: ("Route", [(0, "Nord"), (6, "Est"), [7, "Ouest"]]),
      4: ("Garde-manger", [(1, "Ouest")]),
      5: ("Jardin", [(2, "Ouest")]),
      6: ("Sortie", []),
      7: ("Trou", [(8, "Nord")]),
      8: ("Perdu", [(7, "Sud")])}

fsf ={1: ('https://www.fsf.org', [(2, 'Working Together for Free Software Fund')]), 2: ('https://www.fsf.org/working-together/fund', [(3, '')]), 3: ('https://www.fsf.org/blogs/recent-blog-posts', [(4, 'GNU Press blog')]), 4: ('https://www.fsf.org/blogs/gnu-press/', [(7, "What's new in the GNU Press Shop"), (5, 'GNU Emacs T-shirts available now at the GNU Press Shop')]), 5: ('https://www.fsf.org/blogs/gnu-press/emacs-t-shirts-available-now-at-the-gnu-press-shop', [(6, 'GNU Press')]), 6: ('https://www.fsf.org/blogs/gnu-press', []), 7: ('https://www.fsf.org/blogs/gnu-press/whats-new-in-the-gnu-press-shop', [(8, 'intern')]), 8: ('https://www.fsf.org/about/interns/2019/valessio-brito', [(33, 'Contact Us'), (9, 'FSF financial information')]), 9: ('https://www.fsf.org/about/financial', [(32, 'Our bylaws'), (31, '2005 FSF Relationship Framework'), (10, 'here')]), 10: ('https://www.fsf.org/annual-reports/', [(11, '')]), 11: ('https://www.fsf.org/annual-reports/fy2017/', 
  [(17, 'ongoing series of conversations with free software developers who choose GNU licenses for their work'), 
   (16, 'create a workaround for'), (15, 'joined with dozens of other organizations to raise awareness and organize in support of net neutrality'), (12, 'Privacy Policy')]), 12: ('https://www.fsf.org/about/free-software-foundation-privacy-policy', [(13, 'Privacy Policy Changelog')]), 13: ('https://www.fsf.org/about/free-software-foundation-privacy-policy/privacy-policy-changelog', [(14, 'https://www.fsf.org/about/free-software-foundation-privacy-policy/free-software-foundation-privacy-policy-v1.0')]), 14: ('https://www.fsf.org/about/free-software-foundation-privacy-policy/free-software-foundation-privacy-policy-v1.0', []), 15: ('https://www.fsf.org/blogs/community/today-july-12th-day-of-action-for-net-neutrality', []), 16: ('https://www.fsf.org/blogs/licensing/you-can-now-register-as-a-dmca-agent-without-using-nonfree-javascript', []), 17: ('https://www.fsf.org/blogs/licensing', [(30, 'FSD meeting recap 2024-10-25'), (29, 'FSD meeting recap 2024-10-18'), (28, 'FSD meeting recap 2024-10-11'), (27, 'FSD meeting recap 2024-01-26'), (26, 'FSD meeting recap 2023-12-29'), (25, 'FSD meeting recap 2023-12-22'), (18, 'Licensing & Compliance Lab updates and why we need your support to educate, serve the free software community')]), 18: ('https://www.fsf.org/blogs/licensing/licensing-compliance-lab-updates-and-why-we-need-your-support-to-educate-serve-the-free-software-community', [(19, 'blog post on protecting free software against confusing additional restrictions')]), 19: ('https://www.fsf.org/blogs/licensing/protecting-free-software-against-confusing-additional-restrictions', [(20, 'The Principles of Community-Oriented GPL Enforcement')]), 20: ('https://www.fsf.org/licensing/enforcement-principles', [(24, 'the FSF'), (21, 'Read this article in Chinese.')]), 21: ('https://www.fsf.org/licensing/translations/97625411793e533a5b9e65bd-gpl-7684539f5219', [(22, 'Translations')]), 
  22: ('https://www.fsf.org/licensing/translations', [(23, 'Zensurneid und Nutzungserlaubnis')]), 23: ('https://www.fsf.org/licensing/translations/20050211.de.html', []), 24: ('https://www.fsf.org/blogs/licensing/compliance-situations', []), 25: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2023-12-22', []), 26: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2023-12-29', []), 27: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2024-01-26', []), 28: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2024-10-11', []), 29: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2024-10-18', []), 30: ('https://www.fsf.org/blogs/licensing/fsd-meeting-recap-2024-10-25', []), 31: ('https://www.fsf.org/about/fsf-relationship-framework', []), 
  32: ('https://www.fsf.org/about/fsf-bylaws', []), 33: ('https://www.fsf.org/about/contact/', [(36, 'Mailing address and telephone/fax numbers'), (34, 'Virtually tour our previous office at 51 Franklin Street')]), 
  34: ('https://www.fsf.org/about/contact/tour-2010', [(35, 'Contact the Free Software Foundation')]), 35: ('https://www.fsf.org/about/contact', []), 
  36: ('https://www.fsf.org/about/contact/mailing', [(37, 'here')]), 37: ('https://www.fsf.org/about/ways-to-donate/', [(38, 'donating your car')]), 
  38: ('https://www.fsf.org/associate/car/', [(41, 'Gift a membership'), (40, 'More info'), (39, 'Contact us')]), 39: ('https://www.fsf.org/associate/contact.html', []), 40: ('https://www.fsf.org/associate/about-the-member-forum', []), 41: ('https://www.fsf.org/associate/gift', [(42, 'benefits')]), 42: ('https://www.fsf.org/associate/benefits', [(43, 'compact tri-color bulletin')]), 43: ('https://www.fsf.org/bulletin/', [(44, 'Issue 11 - Fall 2007')]), 
  44: ('https://www.fsf.org/bulletin/2007/fall/', [(49, 'Software Patents Coalition by Ben Klemens'), (48, 'AntiFeatures by Benjamin Mako Hill'), (47, 'GNU Affero GPL by Brett Smith'), (45, 'Interview with Rob Myers by Matt Lee')]), 45: ('https://www.fsf.org/bulletin/2007/fall/rob-myers/', [(46, 'Fall 2007 Bulletin')]), 46: ('https://www.fsf.org/bulletin/2007/fall', []), 47: ('https://www.fsf.org/bulletin/2007/fall/gnu-affero-gpl/', []), 48: ('https://www.fsf.org/bulletin/2007/fall/antifeatures/', []), 49: ('https://www.fsf.org/bulletin/2007/fall/software-patents/', [])}

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
    Renvoie l'ensemble des sommets accessibles depuis d, ainsi que les chemins pour y arriver
    TODO: implementation de Jikstra, potentiellement une autre fonction.
    """
    monde = {d}
    sommetsAccessibles = {sommet[0] for sommet in G[d][1]}
    arcs = {(sommet[0],d) for sommet in G[d][1]}

    while sommetsAccessibles != set():
        nextVertex = sommetsAccessibles.pop()
        monde.add(nextVertex)
        sommetsAccessibles.update({sommet[0] for sommet in G[nextVertex][1] if sommet[0] not in monde})
        arcs.update({(seenVertex[0], nextVertex) for seenVertex in G[nextVertex][1] if seenVertex[0] not in monde})
        # On aurais en effet pu faire un seul parcour, mais c'est comme ca.
    return monde, arcs

def accessiblecheminsJickstra(G,d, useCost:bool=False):
    """
    Retourne l'ensemble des sommets accessibles depuis d, ansi que les chemins calculé
    a l'aide de l'algo de jiskdktraa
    Ici dans la pratique ca fait la meme chose que la version sans jikstra, car tous les couts sont a 1,
    donc la PriorityQoeue est juste une queue comme le set dans l'autre version.
    
    Si useCost est defini a True, alors on prend en compte le cout des chemins reels, par contre faut que le graph soit compatible:

    Graph de la forme {0: ('ici', [(1, 'Nord', 3)]), 1:('sortie', [])}
                                               ^- Cout du chemin
    """
    monde = {d}
    sommetsAccessibles = PriorityQueue()
    f = {d:0}
    arcs = {(sommet[0],d) for sommet in G[d][1]}

    def GetCost(s):
        if useCost:
            return s[2]
        return 1

    # Ici f[d] = 0 mais c'est pour etre un peu general
    for sommet in G[d][1]:
        # On suppose que le cout de chaque chemin est de 1
        sommetsAccessibles.put((f[d] + GetCost(sommet), sommet[0]))
        f[sommet[0]] = f[d] + 1

    while sommetsAccessibles.qsize() != 0:
        cost, nextVertex = sommetsAccessibles.get()
        f[nextVertex] = cost
        monde.add(nextVertex)

        for sommet in G[nextVertex][1]:
            if sommet[0] not in monde:
                sommetsAccessibles.put((f[nextVertex] +GetCost(sommet), sommet[0]))
                arcs.add((sommet[0], nextVertex))

    return monde, arcs

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
    SaveGraph(fsf, "fsf")
    ShowGraphsInData()