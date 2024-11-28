import utils
import LabyTest

def creerchaine(liste):
    chaine = "Chemins possibles : "
    for i in range(len(liste)):
        chaine+=str(liste[i])
        chaine+= " , "
    return chaine

def balade(graphe,entree):
    caseActuelle = entree
    choix = str(entree)
    while utils.arcsortant(graphe,choix) != []:
        
        while choix not in utils.arcsortant(graphe,caseActuelle) and choix.isdigit() == False:
            choix=input(creerchaine(utils.arcsortant(graphe,caseActuelle))+"Quel chemin voulez vous prendre?")
        
        caseActuelle = choix
        print(caseActuelle)
    return "Bravo"

print(balade(LabyTest.g,0))