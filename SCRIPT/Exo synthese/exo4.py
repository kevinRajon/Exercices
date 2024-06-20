tab=[15, 7, 18, 3, 2, 5, 20, 10, 9, 14]
res=0

for i in range(0, 10, 1):
    if tab[i]>=10:
        res=res+1
    else:
        res=res

print(res, "eleves ont obtenu la moyenne.")
        