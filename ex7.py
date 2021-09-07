
def determinerResultatElectionsLegislatives():
    """
    Fonction qui détermine le resultat pour le candidat 1 a l'issus du premier
    tour des elections legislatives de Guignolerie Septentrionale
    """
    
    scoresCandidats = []
    candidatQualifieSecondTour = {}
    
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
    else:
        for i in range(3):
            if (scoresCandidats[i+1] > 50): # Si battu premier tour
                res = "Battu"
            else:
                if (scoresCandidats[0] < 12.5): # Si Eligible second tour
                    candidatQualifieSecondTour["Candidat1"] = scoresCandidats[0]
                    for i in range(3):
                        if (scoresCandidats[i+1] < 12.5):
                            candidatQualifieSecondTour["Candidat{}".format(i+1)] = scoresCandidats[i+1]
                    # for i in range(len(candidatQualifieSecondTour)):
                    print(candidatQualifieSecondTour)
                    
                else:
                    res = "Battu"
        
    return res
                    
             
         

res = determinerResultatElectionsLegislatives()
print("Le verdicte des elections pour le candidat 1 est : {}".format(res))