tab = [21, 65, 36, 48, 78, 2, 98, 47, 63, 54]

# Calcul de la longueur de la liste tab
n = len(tab)

# Boucle principale pour itérer à travers la liste
for i in range(n):
    swapped = False  # Variable pour suivre si des échanges ont eu lieu pendant cette itération

    # Boucle pour comparer les éléments adjacents et les échanger si nécessaire
    # n-i-1 car après chaque itération i, l'élément le plus grand est déjà à sa place finale
    for j in range(0, n-i-1):
        if tab[j] > tab[j+1]:  # Si l'élément courant est plus grand que l'élément suivant
            # Échange des éléments
            tab[j], tab[j+1] = tab[j+1], tab[j]
            swapped = True  # Marquer qu'un échange a eu lieu

    # Si aucun échange n'a eu lieu pendant cette itération, le tableau est trié
    if not swapped:
        break

# Affichage du tableau trié
print(tab)
