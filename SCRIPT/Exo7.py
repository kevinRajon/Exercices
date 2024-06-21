PU = float(input("Saisir le prix du produit: "))
if PU < 20:
    PU = PU + ((10 / 100) * PU)
elif PU < 50:
    PU = PU + ((10 / 100) * PU)
elif PU < 100:
    PU = PU + ((5 / 100) * PU)
else:
    PU = PU + ((2.5 / 100) * PU)

print("Le prix mis à jour est: ", round(PU, 2))
