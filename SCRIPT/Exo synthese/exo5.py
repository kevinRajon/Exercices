tab=[15, 7, 32, 3, 12, 5, 20, 10, 9, 1]

n=len(tab)

print(tab)    

for i in range(0, n-1, 1):
    if tab[i] > tab[i+1]:
        max = tab[i]
        tab[i] = tab[i+1]
        tab[i+1] = max
        
for i in range(0, n-1, 1):
    if tab[i] < tab[i+1]:
        min = tab[i]
        tab[i] = tab[i+1]
        tab[i+1] = min
        
print("La valeur la plus grande est:", max)
print("La valeur la plus petite est:", min)
