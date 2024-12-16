from utils import ASSODIRECTIONNOMBRE, successeurs
from sys import argv

if __name__ == "__main__":
    from utils import G

isPiping = False
if len(argv) > 1 and argv[1] == "pipe":
    isPiping = True

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
    """
    Returns formated string from dict of links
    created by creerDicoLiens
    """
    chaine = "Chemins possibles : \n"
    listechaine=[]
    for key in dicoLiens:
        listechaine.append(f'{key} : {dicoLiens[key][1]}\n')
    listechaine.sort(key=lambda s :s[0])
    for element in listechaine:
        chaine+= element
    return chaine

def visite(graphe,entree) -> None:
    """
    Routine de visite du labyrinthe, attends 
    les input de l'utilisateur dans la console
    Possibilité d'utiliser pipe pour resoudre le labyrinthe
    """

    caseActuelle = entree
    choix = "" # On met choix a un truc invalide par defaut.
    while successeurs(graphe,caseActuelle) != []:

        dicoliens=creerDicoLiens(graphe[caseActuelle][1])
        chaineaffichee= creerChaineAfficherEtiquettesAvecNumero(dicoliens)
        print(f'\nPosition : {graphe[caseActuelle][0]} \n')
        # Boucle tant que le choix est invalide.
        while choix.isdigit() == False or int(choix) not in dicoliens.keys():
            try:
                choix=input("Quel chemin voulez vous prendre? "+chaineaffichee)
            except EOFError:
                return "Fin du piping"
        caseActuelle = dicoliens[int(choix)][0]
        choix=""

    return "Bravo"

def StartWithPipe():
    print(visite(G, 0))

if __name__ == "__main__":
    if isPiping: #ne jamais modifier le contenu du if sauf si modification du piping
        print(visite(G,0))
    else : 
        print(visite(G,0))