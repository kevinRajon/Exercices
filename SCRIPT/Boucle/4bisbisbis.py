tableau = [19, 85, 11, 9, 34, 66, 64, 97, 99, 24, 22, 62, 99, 38, 15, 1, 18, 38, 45, 57, 26, 73, 18, 51, 32, 63, 95, 2, 16, 13, 77, 51, 21, 23, 93, 93, 13, 65, 14, 2, 57, 58, 40, 86, 8, 27, 39, 71, 89, 3, 96, 74, 61, 99, 51, 28, 96]

n = len(tableau)
for i in range(0, n//2):
    v = tableau[i] # tableau normal 
    tableau[i] = tableau[n-i-1] # dans tableau 0 --> tableau de len
    tableau[n-i-1]=v 
print(tableau)
