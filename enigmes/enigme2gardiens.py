class Gardien:
    def __init__(self, verite):
        self.verite = verite  # True pour dire la vérité, False pour mentir

    def repondre(self, autre_gardien, porte_liberté):
        if self.verite:
            return autre_gardien.quel_porte(porte_liberté)
        else:
            return not autre_gardien.quel_porte(porte_liberté)
    
    def quel_porte(self, porte_liberté):
        if self.verite:
            return porte_liberté
        else:
            return not porte_liberté

# Créons les gardiens
gardien1 = Gardien(verite=True)  # Ce gardien dit la vérité
gardien2 = Gardien(verite=False)  # Ce gardien ment

# Supposons que la porte 1 mène à la liberté (True) et la porte 2 mène à la mort (False)
porte_liberté = True

# On pose la question au gardien 1
reponse_gardien1 = gardien1.repondre(gardien2, porte_liberté)

# Selon la réponse du gardien 1, on choisit la porte opposée
if reponse_gardien1:
    porte_choisie = False  # Choisir l'autre porte (porte 2)
else:
    porte_choisie = True  # Choisir l'autre porte (porte 1)

# Affichons le résultat
if porte_choisie == porte_liberté:
    print("Vous avez choisi la porte de la liberté !")
else:
    print("Vous avez choisi la porte de la mort...")

# Output attendu: "Vous avez choisi la porte de la liberté !"
