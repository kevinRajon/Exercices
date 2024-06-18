while True:
    v1 = float(input("Entrez un nombre: "))
    
    while True:
        op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")
        while op !="+" and op!="-" and op!="*" and op!="/" and"stop":
            print("SAISIE INVALIDE")
            op = input("Saisir une opération: + - * / ou 'stop' pour arrêter: ")
        
        if op == "stop":
            print("FIN DES CALCULS")
            break
        
        v2 = float(input("Entrez un autre nombre: "))
        
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
        
        print("Le résultat est:", result)
        v1 = result

