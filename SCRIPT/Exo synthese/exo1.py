a = int(input("Entrer la valeur 1: "))
b = int(input("Entrer la valeur 2: "))
c = int(input("Entrer la valeur 3: "))
somme = (a+b+c)
moyenne = (somme/3)
print("La somme des valeurs est: ", somme)
print("La moyenne des valeurs est: ", round(moyenne, 2))

if a > b and a > c:
    print("La plus grande valeur est: ",  a)
elif b > a and b > c:
    print("La plus grande valeur est: ", b)
else:
    print("La plus grande valeur est: ",  c)

if a<b and a<c:
    print("La plus petite valeur est: ",  a)
elif b<a and b<c:
    print("La plus petite valeur est: ",  b)
else:
    print("La plus petite valeur est: ",  c)
    