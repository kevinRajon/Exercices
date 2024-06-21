tab = [21, 65, 36, 48, 78, 2, 98, 47, 63, 54]

# Calcul de la longueur de la liste tab
n = len(tab)

# Initialisation de l'indice pour la boucle principale
i = 0

# Boucle principale avec while pour itérer à travers la liste
while i < n:
    swapped = False  # Variable pour suivre si des échanges ont eu lieu pendant cette itération

    # Boucle pour comparer les éléments adjacents et les échanger si nécessaire
    # n-i-1 car après chaque itération i, l'élément le plus grand est déjà à sa place finale
    j = 0
    while j < n-i-1:
        if tab[j] > tab[j+1]:  # Si l'élément courant est plus grand que l'élément suivant
            # Utilisation d'une variable temporaire pour échanger les éléments
            temp = tab[j]
            tab[j] = tab[j+1]
            tab[j+1] = temp
            swapped = True  # Marquer qu'un échange a eu lieu
        j += 1

    # Si aucun échange n'a eu lieu pendant cette itération, le tableau est trié
    if not swapped:
        break
    
    # Incrémenter l'indice de la boucle principale
    i += 1

# Affichage du tableau trié
print(tab)
