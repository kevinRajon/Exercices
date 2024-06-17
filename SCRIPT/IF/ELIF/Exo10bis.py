a = float(input("Entrer la valeur 1: "))
b = float(input("Entrer la valeur 2: "))
c = float(input("Entrer la valeur 3: "))

somme = a + b + c
moyenne = somme / 3

print("La somme des valeurs est: ", somme)
print("La moyenne des valeurs est: ", round(moyenne, 2))

valeur= [a, b, c]
valeur_max= max(valeur)
valeur_min= min(valeur)

print("La valeur la plus grande est: ", valeur_max)
print("La valeur la plus petite est: ", valeur_min)