def dechiffrage(message_chiffre):
    correspondance = {
        "2": 'A',   "22": 'B',   "222": 'C',
        "3": 'D',   "33": 'E',   "333": 'F',
        "4": 'G',   "44": 'H',   "444": 'I',
        "5": 'J',   "55": 'K',   "555": 'L',
        "6": 'M',   "66": 'N',   "666": 'O',
        "7": 'P',   "77": 'Q',   "777": 'R',   "7777": 'S',
        "8": 'T',   "88": 'U',   "888": 'V',
        "9": 'W',   "99": 'X',   "999": 'Y',   "9999": 'Z', "0": ' '
    }

    message_clair = ""
    i = 0
    n = len(message_chiffre)

    while i < n:
        message = ""
        while i < n and message_chiffre[i].isdigit():
            message += message_chiffre[i]
            i += 1
        if message in correspondance:
            message_clair += correspondance[message]
        while i < n and not message_chiffre[i].isdigit():
            i += 1

    return message_clair


while True:
    message_chiffre = input(
        "Saisissez votre message chiffré (ou 'q' pour quitter): ").strip()

    if message_chiffre.lower() == 'q':
        break

    message_decode = dechiffrage(message_chiffre)
    print("Message déchiffré:", message_decode)
