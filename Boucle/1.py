print("Gestion du budget")
budget=int(input("Quel est votre budget: "))
while budget > 0:
    print("Vous ne pouvez pas depenser plus de: ", budget)
    depense=int(input("Combien voulez vous depenser: "))

    budget=budget-depense

print("budget depassé de: ", -budget)