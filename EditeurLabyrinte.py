def CreationLabyrinte(nombreSommets : int):
    dico={}
    listeSommets=getListeNomsSommets(nombreSommets)
    for i in range(nombreSommets):
        dico[i]=(listeSommets[i],[])
    for sommet in dico.keys():
        nombreaccessibles = getNombreSommetsAccessibles(dico[sommet][0])
        for _ in range(nombreaccessibles):
            dico[sommet]=getSommetsAccessibles(dico[sommet][0],nombreaccessibles,listeSommets)
    return dico

def getNombreSommets():
    result=""
    while result.isdigit() == False :
        result = input("Combien de sommets dans votre graphe? \n")
    return int(result)

def getListeNomsSommets(nombresommets:int):
    list=[]
    acces=""
    for i in range(nombresommets):
        acces = input(f'Nom sommet {i} ?')
        while acces in list:
            acces = input(f'Nom sommet {i} ?')
        list.append(acces)
    return list

def getEntree():
    return input("Ou voulez vous entrer? \n")
                      
def getNombreSommetsAccessibles(etiquetteSommet):
    result=""
    while result.isdigit() == False:
        result= (input(f'Combiens de sommet accessibles depuis {etiquetteSommet} ? \n'))
    return int(result)



def getSommetsAccessibles(sommet : str, nombreaccessibles : int, listesommet : list):
    list=[]
    acces= ""
    for i in range(nombreaccessibles):
        while acces not in listesommet:
            acces=input(f'Quel sommet sera accessible depuis {sommet} ? \n')
        list.append(acces)
    return list



if __name__ == "__main__":
    CreationLabyrinte(getNombreSommets())

