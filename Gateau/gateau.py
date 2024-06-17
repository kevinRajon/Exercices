import tkinter as tk
from tkinter import messagebox
import random

# Liste des personnes et des gâteaux
people = ["Nadia", "Linda", "Marwan", "Kevin", "Nezha", "Ruzanha", "Iliess", "Esmail", "Youness", "Myriam", "Anna", "Antoine", "Karima", "Marwa"]
cakes = ["Gâteau au yaourt", "Brownie", "Cake aux bananes (Banana Bread)", "Gâteau au chocolat fondant", "Gâteau marbré", "Clafoutis", "Gâteau aux pommes", "Muffins", "Financiers", "Gâteau renversé à l'ananas", "Cookies", "Tarte Tatin", "Gâteau au citron", "Gâteau au fromage blanc", "Tarte au chocolat", "Muffins au chocolat", "Tarte aux fraises sans cuisson", "Pain d'épices", "Moelleux au chocolat", "Gâteau au yaourt marbré", "Tarte au citron meringuée", "Gâteau aux carottes", "Gâteau marbré au chocolat et à la vanille", "Gâteau aux poires", "Gâteau au fromage (Cheesecake)", "Tiramisu", "Gâteau basque", "Gâteau roulé"]

# Fonction pour sélectionner aléatoirement une personne et un gâteau
def select_random():
    selected_person = random.choice(people)
    selected_cake = random.choice(cakes)
    messagebox.showinfo("Sélection Aléatoire", f"Personne: {selected_person}\nGâteau: {selected_cake}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Sélection Aléatoire")

# Ajouter un bouton pour déclencher la sélection
select_button = tk.Button(root, text="Sélectionner", command=select_random)
select_button.pack(pady=20)

# Démarrer la boucle principale de l'interface
root.mainloop()