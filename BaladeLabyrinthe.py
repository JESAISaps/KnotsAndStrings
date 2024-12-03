import utils
from utils import G, ASSODIRECTIONNOMBRE

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



def visite(graphe,entree):
    caseActuelle = entree
    choix = "-2"
    while utils.successeurs(graphe,caseActuelle) != []:

        dicoliens=creerDicoLiens(graphe[caseActuelle][1])
        chaineaffichee= creerChaineAfficherEtiquettesAvecNumero(dicoliens)

        while choix.isdigit() == False or int(choix) not in dicoliens.keys():
            choix=input("Quel chemin voulez vous prendre? "+chaineaffichee)
        
        caseActuelle = dicoliens[int(choix)][0]
        print(graphe[caseActuelle][0]+"\n")
        choix="-2"

    return "Bravo"

if __name__ == "__main__":
    print(visite(G,0))