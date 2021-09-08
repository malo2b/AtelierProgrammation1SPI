
def determinerResultatElectionsLegislatives():
    """
    Fonction qui détermine le resultat pour le candidat 1 a l'issus du premier
    tour des elections legislatives de Guignolerie Septentrionale
    """
    
    RESULTAT_MIN_TOUR2 = 12.5
    
    scoresCandidats = []
    res = ""
    
    for i in range(4):
        while True:
            try:
                flag = float(input("Veuillez saisir le score du candidat {} : ".format(i+1)))  
                if (flag >= 0):
                    scoresCandidats.append(flag)
                    break   
                else:
                    print("Veuillez faire une saisie valide !")

            except ValueError:
                print("Veuillez faire une saisie valide !")

    if (scoresCandidats[0] > 50): # Si élu premier tour
        res = "Elu"
    elif max(scoresCandidats) > 50: # Si battu au premier tour
        res = "Battu"
    elif (scoresCandidats[0] > RESULTAT_MIN_TOUR2): # Si Eligible second tour
        res = "Favorable"
        idx = 1
        while idx < len(scoresCandidats) and res == "Favorable":
            if (scoresCandidats[idx] > RESULTAT_MIN_TOUR2) and (scoresCandidats[idx] > scoresCandidats[0]):
                res = "Défavorable"  
            idx = idx + 1       
    else:
        res = "Battu"
        
    return res

res = determinerResultatElectionsLegislatives()
print("Le verdicte des elections pour le candidat 1 est : {}".format(res))