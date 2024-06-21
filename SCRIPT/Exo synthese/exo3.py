# Algorithme visant a detemliner quelle valeur d'un tableau est paire ou impaire

tab = [51, 94, 25, 64, 47, 82, 15, 46, 78, 7] #soit un tableau de 10 entier

for i in range(0, 10, 1): #on parcour le tableau de la 1ere à la dernière valeur
    if tab[i]%2==0: #si la valeur est divisible par 2 sans reste alors elle est paire
        print(tab[i], "est pair") 
    else:           #sinon elle est impaire
        print(tab[i], "est impair")



#ou

tab = [51, 94, 25, 64, 47, 82, 15, 46, 78, 7]
i=-1

while i<9:
    i+=1
    if tab[i]%2==0:
        print(tab[i], "est pair")
    else:
        print(tab[i], "est impair")