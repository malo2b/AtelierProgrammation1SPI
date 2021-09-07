
def calculerFraisMensuelsVoiture():
    """
    fonction de calcule des frais mensuels d'utilisation des voitures
    """
    
    # Constantes #

    PALIER_CYLINDREE_ESSENCE = 2000
    
    CONSOMATION_VEHICULE_ESSENCE_SUP_PALIER = 10
    CONSOMATION_VEHICULE_ESSENCE_INF_PALIER = 8
    CONSOMATION_VEHICULE_DIESEL = 8
    
    SURCOUT_ESSENCE = 1.5
    SURCOUT_DIESEL = 1.7
    
    # Saisie Utilisateur #
    while True:
        try:
            nbrKmParAn = int(input("Veuillez saisir le nombre de km parcouru en une année : "))  
            nbrKmParMois = nbrKmParAn / 12
            break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    while True:
        try:
            carburant = str(input("Veuillez saisir le type de carburant [E/D] : "))
            if (len(carburant) == 1 and (carburant == "E" or carburant == "D")):
                break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    while True:
        try:
            cylindree = int(input("Veuillez saisir la cylindrée du véhicule en cm3: "))  
            break   
        except ValueError:
            print("Veuillez faire une saisie valide !")

    while True:
        try:
            prixCarburant = float(input("Veuillez saisir le prix du carburant : "))  
            break   
        except ValueError:
            print("Veuillez faire une saisie valide !")


    # Traitement #
    
    if (carburant == "E"): # Si vehicule essence
        if (cylindree >= PALIER_CYLINDREE_ESSENCE): # Si moteur > 2L
            frais = CONSOMATION_VEHICULE_ESSENCE_SUP_PALIER * prixCarburant  * nbrKmParMois / 100 # Prix Carburant
            frais *= SURCOUT_ESSENCE # Ajout surcout entretient
            
        else: # Si moteur < 2L
            frais = CONSOMATION_VEHICULE_ESSENCE_INF_PALIER * prixCarburant  * nbrKmParMois / 100 # Prix Carburant
            frais *= SURCOUT_ESSENCE # Ajout surcout entretient

    else: # Si vehicule diesel
        frais = CONSOMATION_VEHICULE_DIESEL * prixCarburant  * nbrKmParMois / 100
        frais *= SURCOUT_DIESEL # Ajout surcout entretient

    return frais
    
fraisMensuels = calculerFraisMensuelsVoiture()
print ("Le montant des frais de votre véhicule ce mois-ci s'éleve à {} euros".format(fraisMensuels))