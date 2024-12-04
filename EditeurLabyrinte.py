def CreationLabyrinte(nombreSommets : int):
    dico={}
    listeSommets=getNomSommets(nombreSommets)
    for i in range(nombreSommets):
        dico[i]=(listeSommets[i],[])
    for sommet in dico.keys():
        nombreaccessibles = getNombreSommetsAccessibles(dico[sommet][0])
        for _ in range(nombreaccessibles):
            dico[sommet]=getSommetsAccessibles(dico[sommet][0],nombreaccessibles)

#VERIFIER LE TYPE DES SOMMET ACCESSIBLES !!!!!!!!

def getNombreSommets():
    return int(input("Combien de sommets dans votre graphe? \n"))

def getNomSommets(nombresommets):
    list=[]
    for i in range(nombresommets):
        list.append(input(f'Nom sommet {i} ?'))
    return list

def getEntree():
    return input("Ou voulez vous entrer? \n")
                      
def getNombreSommetsAccessibles(etiquetteSommet):
    return int(input(f'Combiens de sommet accessibles depuis {etiquetteSommet} ? \n'))

def getSommetsAccessibles(sommet, nombreaccessibles):
    list=[]
    for i in range(nombreaccessibles):
        list.append(input(f'Quel sommet sera accessible depuis {sommet} ? \n'))
    return list


if __name__ == "__main__":
    CreationLabyrinte(getNombreSommets())

