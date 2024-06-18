# Boucle infinie pour demander un premier nombre
while True:
    try:
        # Demande à l'utilisateur d'entrer un nombre
        v1 = float(input("Entrez un nombre: "))
        result = float(v1)  # Cette ligne est redondante car v1 est déjà un float
        break  # Sort de la boucle si la conversion est réussie
    except ValueError:
        # Message d'erreur en cas de saisie incorrecte
        print("Saisie incorrecte")

# Boucle infinie pour demander une opération jusqu'à ce que l'utilisateur tape 'stop'
while True:
    op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")
    # Boucle interne pour valider l'opération saisie
    while op != "+" and op != "-" and op != "*" and op != "/" and op != "stop":
        print("SAISIE INVALIDE")
        op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")

    if op == "stop":
        # Arrête le programme si l'utilisateur saisit 'stop'
        print("FIN DES CALCULS")
        break
    else:
        # Boucle pour demander le deuxième nombre jusqu'à ce qu'une saisie correcte soit effectuée
        while True:
            try:
                v2 = float(input("Entrez un nombre: "))
                result = float(v2)  # Cette ligne est redondante car v2 est déjà un float
                break  # Sort de la boucle si la conversion est réussie
            except ValueError:
                # Message d'erreur en cas de saisie incorrecte
                print("Saisie incorrecte")

        # Effectue l'opération choisie
        if op == "+":
            result = v1 + v2
        elif op == "-":
            result = v1 - v2
        elif op == "*":
            result = v1 * v2
        elif op == "/":
            if v2 != 0:
                result = v1 / v2
            else:
                # Gestion de l'erreur division par zéro
                print("Erreur: Division par zéro")
                continue  # Retourne au début de la boucle pour demander une nouvelle opération sans changer v1

        # Affiche le résultat de l'opération
        print("Le résultat est:", result)
        v1 = result  # Met à jour v1 pour la prochaine opération
