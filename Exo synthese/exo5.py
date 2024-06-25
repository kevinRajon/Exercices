# Algorithme visant à determiner la plus petite et la plus grande valeur d'un tableau 

tab=[1, 7, 32, 3, 12, 5, 20, 32, 9, 2]
n=len(tab) # Variable = a la taille du tableau
print(tab)    # Affichage du tableau

for i in range(0, n-1, 1):    # Boucle pour determiner la valeur max
    if tab[i] > tab[i+1]:     # Compare les éléments consécutifs
        max = tab[i]          # Stocke la valeur maximale actuelle
        tab[i] = tab[i+1]     # Si la valeur 1 est plus grande que la valeur 2
        tab[i+1] = max        # La valeur sera stockée dans max
        
for i in range(0, n-1, 1):    # Idem pour la valeur mini
    if tab[i] < tab[i+1]:
        min = tab[i]
        tab[i] = tab[i+1]
        tab[i+1] = min
        
print("La valeur la plus grande est:", max)
print("La valeur la plus petite est:", min)  # Affichage des valeurs mini et maxi 
