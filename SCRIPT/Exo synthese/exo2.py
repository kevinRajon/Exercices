pr100=float(input("Saisissez un pourcentage de voix  : "))

if pr100<5:
    print("Candidat eliminé")
elif pr100<50:
    print("Candidat qualifié au 2nd tour")
else:
    print("Candidat élu")

