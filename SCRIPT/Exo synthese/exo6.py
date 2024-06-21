nb=int(input("Entrez une valeur: "))
tab=[15, 7, 32, 3, 12, 5, 32, 10, 9, 1]
res=0


for i in range(0, 10, 1):
    if nb==tab[i]:
        res=res+1
        
if res > 0: 
    print(f"{nb} apparait {res} fois dans le tableau")
else:
    print(f"{nb} n'est pas dans le tableau")