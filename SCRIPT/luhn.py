tab = [4,1,2,5,2,5,2,3,5,8,7,6,8,0,0,9]

tab.reverse()


for i in range(0, n, 2):
    tab[i] *=2
    if tab[i] > 9:
        tab[i] = tab[i]-9


if res%10 == 0:
    print("Numero valide")
else:
    print("Numero Invalide")
    

