# Algorithme visant à calculer la moyenne et la somme de  3 valeurs
# Determine ensuite la plus grande et la plus petite des valeurs

a = int(input("Entrer la valeur 1: "))
b = int(input("Entrer la valeur 2: "))   # On demande a l'utilisateur d'entrer 3 valeurs
c = int(input("Entrer la valeur 3: "))
somme = (a+b+c)    # On addittione les 3 valeurs
moyenne = (somme/3)   # On fait la moyenne des valeurs
print("La somme des valeurs est: ", somme)
print("La moyenne des valeurs est: ", round(moyenne, 2)) # affichage de la moyenne arrondie 

if a > b and a > c:
    print("La plus grande valeur est: ",  a)
elif b > a and b > c:                         # Comparaison des valeurs
    print("La plus grande valeur est: ", b)   # Determination de la plus grande valeur 
else:
    print("La plus grande valeur est: ",  c)

if a<b and a<c:
    print("La plus petite valeur est: ",  a)
elif b<a and b<c:                               # Comparaison des valeurs
    print("La plus petite valeur est: ",  b)    # Determination de la plus petite valeur
else:
    print("La plus petite valeur est: ",  c)
    