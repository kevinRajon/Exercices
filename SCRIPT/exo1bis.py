v1 = (input("Saisir une 1ere variable: "))
v2 = (input("Saisir une 2eme variable: "))
print(f"Variable 1: {v1} Variable 2: {v2}")
v3 = v1
v1 = v2
v2 = v3
print(f"Variable 1: {v1} Variable 2: {v2}")