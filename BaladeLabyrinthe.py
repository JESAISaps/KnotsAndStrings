from utils import ASSODIRECTIONNOMBRE, successeurs
if __name__ == "__main__":
    from utils import G

def creerDicoLiens(listechoix:list[tuple[int, str]]) -> dict[str, list[tuple[int, str]]]:
    """
    Renvoie un dictionnaire qui associe le choix de l'utilisateur 
    à une case parmis celles accessibles à leur niveau 
    """
    dico={}
    for element in listechoix:
        dico[ASSODIRECTIONNOMBRE[element[1]]]= element
    return dico

def creerChaineAfficherEtiquettesAvecNumero(dicoLiens) -> str:
    chaine = "Chemins possibles : \n"
    for key in dicoLiens:
        chaine += str(key) + " : "
        chaine += dicoLiens[key][1] + "\n"
    return chaine

def visite(graphe,entree) -> None:
    caseActuelle = entree
    choix = "" # On met choix a un truc invalide par defaut.
    while successeurs(graphe,caseActuelle) != []:

        dicoliens=creerDicoLiens(graphe[caseActuelle][1])
        chaineaffichee= creerChaineAfficherEtiquettesAvecNumero(dicoliens)

        while choix.isdigit() == False or int(choix) not in dicoliens.keys():
            choix=input("Quel chemin voulez vous prendre? "+chaineaffichee)
        
        caseActuelle = dicoliens[int(choix)][0]
        print(graphe[caseActuelle][0]+"\n")
        choix=""

    return "Bravo"

if __name__ == "__main__":
    print(visite(G,0))