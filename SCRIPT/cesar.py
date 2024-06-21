def algo_cesar(mess, dec, sens):
    # Tableaux pour les lettres minuscules et majuscules
    tab_min = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    tab_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mess_chiffre = []  # tableau pour stocker les caractères chiffrés
    
    for car in mess:
        if car.islower():  # Si le caractère est minuscule
            tab = tab_min
        elif car.isupper():  # Si le caractère est majuscule
            tab = tab_maj
        else:
            # Si ce n'est pas une lettre, ne pas chiffrer
            mess_chiffre.append(car)
            continue
        
        if sens == '+':
            nouvel_index = (tab.index(car) + dec)
        elif sens == '-':
            nouvel_index = (tab.index(car) - dec)
        
        car_chiffre = tab[nouvel_index]
        mess_chiffre.append(car_chiffre)
    
    return (mess_chiffre)

# Demander à l'utilisateur de saisir le message, le décalage et le sens du décalage
mess = input("Saisissez votre message: ")
dec = int(input("Saisissez la valeur de décalage: "))
sens = input("Saisissez le sens de décalage (+ pour décaler vers la fin, - pour décaler vers le debut) : ")

# Appeler la fonction de chiffrement César
mess_chiffre = algo_cesar(mess, dec, sens)

# Afficher le message chiffré
print("Message chiffré :", mess_chiffre)


