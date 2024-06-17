print("Facture photocopieur")
NB = float(input("Combien de photocopies :  "))
if NB <= 10:
    NB = (0.1*NB)
elif NB <= 20:
    NB = (10*0.1)+((NB-10)*0.08)
elif NB <= 50:
    NB = (10*0.1)+(10*0.08)+((NB-20)*0.06)
else:
    NB = (10*0.1)+(10*0.08)+(30*0.06)+((NB-50)*0.03)
print("Votre facture est de: ", round(NB, 2))
