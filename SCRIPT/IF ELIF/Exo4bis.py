q = float(input("Quanttité: "))
print("La quantité de produit est: ", q)
pu = float(input("Prix produit: "))
print("Le pri unitaire est de: ", pu)
mth = q*pu
print(f"Le prix total HT est de {q*pu}")
if mth < 200: 
    mthr=mth-(mth*(2.5/100))
elif mth < 400: 
    mthr=mth-(mth*(5/100))
elif mth < 700: 
    mthr=mth-(mth*(7.5/100))
else: 
    mthr=mth-(mth*(10/100))
tva=(20/100)*mthr
print("Le montant de la TVA est de : ",tva)
print(f"Le montant TTC est de: ", mthr+tva)    