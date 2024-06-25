# Algorithme visant à determiner combien d'eleve ont eu la moyenne
# Note des élèves dans un tableau 

tab=[15, 7, 18, 3, 2, 5, 20, 10, 9, 14]
res=0              # Variable de stockage (compteur)

for i in range(0, 10, 1):
    if tab[i]>=10:    # Si la valeur du tableau est >= 10
        res=res+1  # Mon compteur est incrémenté de 1
    else:
        res=res # Sinon mon compteur ne bouge pas 

print(res, "eleves ont obtenu la moyenne.")
        