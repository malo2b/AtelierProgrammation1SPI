def calculerFactureReprographie(): 
    """
    Fonction qui détermine le prix de la factrure de la reprographie
    """
    
    # CONSTANTES #
    TARIF1 = 0.1
    TARIF2 = 0.09
    TARIF3 = 0.08
    BORNE1 = 10
    BORNE2 = 30
      
    # Variables #
    facture = 0
    
    while True:
        try:
            nbrPhotocopies = int(input("Veuillez saisir le nombre de photocopies : "))  
            break   
        except ValueError:
            print("Veuillez saisir un nombre entier !")
    
        
    if (nbrPhotocopies <= 10):
        facture = nbrPhotocopies * TARIF1
    elif (nbrPhotocopies <= 30):
        facture = BORNE1 * TARIF1 + (nbrPhotocopies - BORNE1) * TARIF1
    else:
        facture = TARIF3 * (nbrPhotocopies - BORNE2) + (BORNE2 - BORNE1) * TARIF2 + BORNE1 * TARIF1
   
    return round(facture,2)
        
print(calculerFactureReprographie())