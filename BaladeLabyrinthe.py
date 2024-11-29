import utils
import LabyTest


ASSODIRECTIONNOMBRE = {"Nord":1, "Sud":2, "Est":3, "Ouest":4}


def creerDicoLiens(listechoix:list[tuple[int, str]]):
    """
    Renvoie un dictionnaire qui associe le choix de l'utilisateur à une case parmis celles accessibles à leur niveau 
    """
    dico={}
    #compteur = 1
    for element in listechoix:
        dico[ASSODIRECTIONNOMBRE[element[1]]]= element
        #compteur += 1
    return dico


def creerChaineAfficherEtiquettesAvecNumero(dicoLiens):
    chaine = "Chemins possibles : \n"
    for key in dicoLiens:


        chaine += str(key) + " : "
        chaine += dicoLiens[key][1] + "\n"
    return chaine



def balade(graphe,entree):
    caseActuelle = entree
    choix = "-1"
    while utils.successeurs(graphe,caseActuelle) != []:

        dicoliens=creerDicoLiens(graphe[caseActuelle][1])
        chaineaffichee= creerChaineAfficherEtiquettesAvecNumero(dicoliens)

        while choix.isdigit() == False or int(choix) not in dicoliens.keys():
            choix=input("Quel chemin voulez vous prendre? "+chaineaffichee)
        
        caseActuelle = dicoliens[int(choix)][0]
        print(graphe[caseActuelle][0]+"\n")
        choix="-1"

    return "Bravo"

g = { 0: ("Bienvenue dans ce monde!", [(1, "Nord"), (2, "Est"), (3, "Sud")]),
      1: ("Vous êtes dans la salle à manger.", [(0, "Sud"), (4, "Est")]),
      2: ("Vous êtes sur la terrasse, sous le préau.", [(5, "Est"), (0, "Ouest")]),
      3: ("Vous êtes sur la route, devant la maison.", [(0, "Nord"), (6, "Est")]),
      4: ("Vous vous trouvez dans le garde-manger.", [(1, "Ouest")]),
      5: ("Vous êtes dans le jardin.", [(2, "Ouest")]),
      6: ("Vous êtes sorti du monde, bravo!", [])}



if __name__ == "__main__":
    print(balade(LabyTest.g,0))