print("Saisir votre note sur 20")
NOTE = float(input("Saisir votre note "))
if NOTE <= 5:
    print("Vous avez E")
elif NOTE <= 8:
    print("Vous avez D")
elif NOTE <= 11:
    print("Vous avez C")
elif NOTE <= 14:
    print("Vous avec B")
else: 
    print("Vous avez A")

