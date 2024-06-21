print("Saisir votre note sur 20")
NOTE = float(input("Saisir votre note "))
if NOTE <= 5:
    print("Vous avez E")
elif 5 < NOTE <= 8:
    print("Vous avez D")
elif 8 < NOTE <= 11:
    print("Vous avez C")
elif 11 < NOTE <= 14:
    print("Vous avec B")
else: 
    print("Vous avez A")

