def calculerFraisPortuaire():
    """
    Fonction qui a pour but de calculer les frais
    portuaires annuels en fonction de la longueur
    et de la catégorie du bateau
    """
    
    # Constantes #
    TARIF_PALIER_1 = 100
    TARIF_PALIER_2 = 200
    TARIF_PALIER_3 = 400
    TARIF_PALIER_4 = 600
    
    LONGUEUR_BATEAU_PALIER_1 = 5 # Bornes longueur en m exclue
    LONGUEUR_BATEAU_PALIER_2 = 10 # 5m inclus 10m inclus
    LONGUEUR_BATEAU_PALIER_3 = 12 # 12m inclus 

    TAXE_CATEGORIE_1 = 100
    TAXE_CATEGORIE_2 = 150
    TAXE_CATEGORIE_3 = 250
   
   # Saisie #
   
    while True:
        try:
            nomBateau = str(input("Veuillez saisir le nom de votre bateau : "))  
            break   
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    while True:
        try:
            longueurBateau = int(input("Veuillez saisir la longueur de votre bateau : "))  
            if (longueurBateau > 0 and longueurBateau < 900):
                break   
            else:
                print("Veuillez saisir la vrai taille de votre bateau")
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    while True:
        try:
            categorieBateau = int(input("Veuillez saisir la catégorie de votre bateau : ")) 
            if (categorieBateau >= 1 and categorieBateau <= 3):
                break   
            else:
                print("Veuillez saisir la catégorie de votre bateau (etre 1 et 3)")
        except ValueError:
            print("Veuillez faire une saisie valide !")
            
    # Calcul cout annuel addition de la taxe et du cout mensuel multiplié aux 12 mois
    
    # Determiner cout annuel sans taxe
    if (longueurBateau < LONGUEUR_BATEAU_PALIER_1):
        coutAnnuelSansTaxe = TARIF_PALIER_1
    elif (longueurBateau <= LONGUEUR_BATEAU_PALIER_2):
        coutAnnuelSansTaxe = TARIF_PALIER_2
    elif (longueurBateau <= LONGUEUR_BATEAU_PALIER_3):
        coutAnnuelSansTaxe = TARIF_PALIER_3
    else:
        coutAnnuelSansTaxe = TARIF_PALIER_4

    coutAnnuelSansTaxe *= 12
        
    # Ajout de la taxe en fonction de la catégorie du bateau
    if (categorieBateau == 1):
        coutAnnuel = coutAnnuelSansTaxe + TAXE_CATEGORIE_1
    elif (categorieBateau == 2):
        coutAnnuel = coutAnnuelSansTaxe + TAXE_CATEGORIE_2
    else:
        coutAnnuel = coutAnnuelSansTaxe + TAXE_CATEGORIE_3
        
    print("le coût annuel d’une place au port pour le voilier {} est de {} euros".format(nomBateau, coutAnnuel))
        
calculerFraisPortuaire()