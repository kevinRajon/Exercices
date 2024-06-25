# Algorithme pour election d'un candidat

pr100=float(input("Saisissez un pourcentage de voix  : ")) # On fait entrer un % à l'utilisateur

if pr100<5:
    print("Candidat eliminé")
elif pr100<50:
    print("Candidat qualifié au 2nd tour")  # Selon le pourcentage on affiche un message
elif pr100<=100:
    print("Candidat élu")
else:
    print("Pourcentage incorrect")

