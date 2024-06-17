tab=[1,2,3,4,5,6,7,8,9,0]

var=10

for i in range(var//2):
    tab[i], tab[var - 1 - i] = tab[var - 1 - i], tab[i]
    
print(tab)
