def saisir_CB():
    while True:
        saisie = input("Veuillez entrer une chaîne de 16 caractères : ")
        if len(saisie) == 16 and saisie.isdigit():
            return [int(ch) for ch in saisie]
        else:
            print("Erreur")


tab = saisir_CB()
n = len(tab)


for i in range(0, n, 2):
    tab[i] *= 2
    if tab[i] > 9:
        tab[i] -= 9

res = sum(tab)

if res % 10 == 0:
    print("La vérification Luhn a réussi: numéro valide.")
else:
    print("La vérification Luhn a échoué: numéro invalide.")
