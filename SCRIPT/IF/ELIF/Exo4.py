print("Calcul de remise selon quantité")
Q = float(input("Saississez la quantité de produit: "))
print("Quantité: ", Q)
PUHT = float(input("Saisissez le prix HT: "))
print("Prix HT: ", PUHT)
QPHT = Q*PUHT
print("Le prix total HT est: ", QPHT)
if QPHT < 200:
    QPHT = (QPHT-(QPHT*(2.5/100)))
elif QPHT < 400:
    QPHT = (QPHT-(QPHT*(5/100)))
elif QPHT < 700:
    QPHT = (QPHT-(QPHT*(7.5/100)))
else:
    QPHT = (QPHT-(QPHT*(10/100)))

MTVA = (20/100)*QPHT
print("Le montant de la TVA est: ", MTVA)
print("Le montant TTC remisé est: ", QPHT+MTVA)
