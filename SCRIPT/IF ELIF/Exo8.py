Q = int(input("Veuillez saisir une quantité de produits : "))
LIV = str(input("Veuillez choisir un mode de livraison (rapide ou normal) : "))

if LIV == "rapide":
    if Q < 50:
        print("Livraison en 2 jours")
    elif Q < 100:
        print("Livraison en 3 jours")
    else:
        print("Livraison en 5 jours")

elif LIV == "normal":
    if Q < 50:
        print("Livraison en 4 jours")
    elif Q < 100:
        print("Livraison en 5 jours")
    else:
        print("Livraison en 7 jours")
