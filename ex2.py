

def reconnaitreCaractere(caractere):
    """
    Méthode qui détermine si un caractère ASCII est un 
    caractère majuscule, minuscule, un chiffre ou caractère spécial*
    """
    
    resultat = ""
    
    if (caractere >= 'a' and caractere <= 'z'):
        resultat = 'Lettre minuscule'
    elif (caractere >= 'A' and caractere <= 'Z'):
        resultat = 'Lettre majuscule'
    elif (caractere >= '0' and caractere <= '9'):
        resultat = 'Chiffre'
    elif (ord(caractere) >= 0 and ord(caractere) <= 127):
        resultat = 'Caractère special'
    else:
        resultat = 'Caractère ASCII etendu'
    
    return(resultat)
    
print("Saisir un caractère : ")
caractereAReconnaitre = input()
print(reconnaitreCaractere(caractereAReconnaitre))