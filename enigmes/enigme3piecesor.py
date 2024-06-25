sac1 = [9.5, 9.5, 9.5, 9.5, 9.5]
sac2 = [10, 10, 10, 10, 10]
sac3 = [10, 10, 10, 10, 10]


def deuxPlateaux(sac1, sac2, sac3):
    if sum(sac1) < sum(sac2):
        return("Les fausses pièces sont dans le sac 1")
    elif sum(sac1) == sum(sac2):
        return("Les fausses pieces sont dans le sac 3")
    else:
        return("Les fausse pièces sant dans le sac 2 ")
        
fauxsac= deuxPlateaux(sac1, sac2, sac3)

print(fauxsac)




