# Initialisation du premier nombre en dehors de la boucle principale
v1 = float(input("Entrez un nombre: "))

while True:
    # Demander l'opération à effectuer
    op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")
    
    # Validation de l'opération saisie
    while op not in ["+", "-", "*", "/", "stop"]:
        print("SAISIE INVALIDE")
        op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")
             
    # Arrêter le programme si l'utilisateur saisit 'stop'
    if op == "stop":
        print("FIN DES CALCULS")
        break
        
    # Saisir le deuxième nombre pour l'opération
    v2 = float(input("Entrez un autre nombre: "))
        
    # Effectuer l'opération en fonction de l'entrée utilisateur
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
            print("Erreur: Division par zéro")
        
    # Afficher le résultat et mettre à jour v1 pour l'opération suivante
    print("Le résultat est:", result)
    v1 = result
