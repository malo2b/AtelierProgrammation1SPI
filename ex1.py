# Méthode qui retourne un salaire mensuel en tenant compte du 
# salaire hopraire, du nombre d'heure et de la majoration des
# heures supplémentaires
def calculerSalaireMensuel(): 
    SALAIREHONORAIRE = 10 # Salaire horaire
    NBRHEURES = 250 # nombre d'heures mensuelles
    salaireMensuel = 0 # déclaration et initialisation de la variable du salaire mensuel 
                
    if (NBRHEURES <= 160):
        salaireMensuel = SALAIREHONORAIRE * NBRHEURES
    elif (NBRHEURES <= 200):
        salaireMensuel = SALAIREHONORAIRE * 160 + SALAIREHONORAIRE * 1.25 * (NBRHEURES - 160)
    else:
        salaireMensuel = SALAIREHONORAIRE * 1.5 * (NBRHEURES - 200) + 40 * SALAIREHONORAIRE * 1.25 + 160 * SALAIREHONORAIRE
   
    return salaireMensuel
        
print(calculerSalaireMensuel()) 