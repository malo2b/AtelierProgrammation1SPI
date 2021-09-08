def determinerFamilleTarif():
    """
    Fonction qui permet de déterminer la famille de tarif auquel
    aura droit un conducteur en fonction de sa situation
    """
    
    # Constantes #
    COULEURS_MALUS = [
        "Bleu",     # 0 pt
        "Vert",     # 1 pt
        "Orange",   # 2 pt
        "Rouge",    # 3 pt
    ]
    AGE_PERMIS_CONDUIRE = 18
    AGE_MAXIMAL_ASSURABLE = 200
    # Variables #
    
    pointsMalusAssurance = 1 # -25ans = 1pt, -2ans permis = 1pt, 1pt par accident
    age = 0                    
    nbrAccidents = 0
    plus2ansPermis = False
    plus1anAnciennete = False
        
    # Saisie #
    
    while True:
        try:
            age = int(input("Veuillez saisir votre age : "))  
            if age < AGE_PERMIS_CONDUIRE:
                print("Vous n'etes pas en age d'assurer un véhicule !")
            elif age <= 0 or age > AGE_MAXIMAL_ASSURABLE:
                print("Veuillez faire une saisie valide !")
            else:
                break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
        
    while True:
        try:
            nbrAccidents = int(input("De combien d'accident avez vous étés responsable ? : "))  
            if nbrAccidents < 0:
                print("Veuillez faire une saisie valide !")
            else:
                break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    while True:
        try:
            saisie = str(input("Avez vous votre permis depuis plus de 2 ans ? [O/N] : "))  
            if len(saisie) != 1 and (saisie != "O" or saisie != "N"):
                print("Veuillez faire une saisie valide !")                
            else:
                if saisie == "O":
                    plus2ansPermis = True
                break   
        except ValueError:
            print("Veuillez faire une saisie valide !")

    while True:
        try:
            saisie = str(input("Etes vous chez nous depuis plus d'un an ? [O/N] : "))  
            if len(saisie) != 1 and (saisie != "O" or saisie != "N"):
                print("Veuillez faire une saisie valide !")                
            else:
                if saisie == "O":
                    plus1anAnciennete = True
                break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
        
    # Traitement #
        
    if age <  25:               # -25ans
        pointsMalusAssurance = pointsMalusAssurance + 1
    if not plus2ansPermis:      # -2ans de permis
        pointsMalusAssurance = pointsMalusAssurance + 1
    pointsMalusAssurance = pointsMalusAssurance + nbrAccidents
    
    if pointsMalusAssurance > 3:
        res = "Refusé !"
    else:
        if plus1anAnciennete:
            pointsMalusAssurance = 0
        res = "Vous etes éligibles au tarif \"{}\"".format(COULEURS_MALUS[pointsMalusAssurance])
       
    return res 

print(determinerFamilleTarif())