
j1 = int(input("Entrer la jour 1: "))
m1 = int(input("Entrer le mois 1: "))
a1 = int(input("Entrer l'année 1: "))
j2 = int(input("Entrer la jour 2: "))
m2 = int(input("Entrer le mois 2: "))
a2 = int(input("Entrer l'année 2: "))

print(f"La première date est : {j1}/{m1}/{a1}")
print(f"La deuxième date est : {j2}/{m2}/{a2}")

if a1 > a2:
    print("La deuxième date est inférieure")
elif a1 < a2:
    print("La première date est inférieure")
else: 
    if m1 > m2:
        print("La deuxième date est inférieure")
    elif m1 < m2:
        print("La première date est inférieure")
    else:  
        if j1 > j2:
            print("La deuxième date est inférieure")
        elif j1 < j2:
            print("La première date est inférieure")
        else:  
            print("Les deux dates sont identiques")