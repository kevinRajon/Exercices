tab=[15, 7, 32, 3, 12, 5, 32, 10, 9, 1] # Soit un tableau de 10 valeurs 
nb=int(input("Entrez une valeur: ")) #On fait entrer une valeur à l'utilisateur
res=0 # res est un stock (compteur d'appartition)


for i in range(0, 10, 1): # On parcours le tableau
    if nb==tab[i]:        # Si la valeur de l'utilisateur est égale a la valeur du tableau 
        res=res+1         # On stock l'information dans un compteur
        
if res > 0: 
    print(f"{nb} apparait {res} fois dans le tableau")
else:                     # Affichage du nombre de fois que la valeur est dans le tableau 
    print(f"{nb} n'est pas dans le tableau")