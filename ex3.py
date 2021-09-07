def estImposable():
    """
    Dit si une personne est imposable en fonction de son age et de son sexe
    """
    age = 0
    estFemme = False
    saisie = ""
    res = ""
    
    age = int(input("Veuillez saisir votre age : "))
    saisie = str(input("\nEtes vous un Homme ou une Femme [H/F] : "))
    if (saisie == "F"):
        estFemme = True
    elif (saisie != "H"):
        res = "Veuillez saisir un caractère valide !"
        estFemme = None
    
    if ((not estFemme and age >= 20) or (estFemme and age >= 18 and age <= 35) and estFemme != None):
        res = "Vous êtes imposable"
    elif (estFemme != None):
        res = "Vous n'êtes pas imposable"
        
    return res
        
print(estImposable())    