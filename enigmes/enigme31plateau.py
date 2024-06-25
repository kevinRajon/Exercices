sac3 = [9.5, 9.5, 9.5, 9.5, 9.5]
sac2 = [10, 10, 10, 10, 10]
sac1 = [10, 10, 10, 10, 10]

def unplateau(sac1, sac2, sac3):
    if sum(sac1)+sum(sac2)>sum(sac1)+sum(sac1):
        return("Les fausses pieces sont dans le sac 1")
    elif sum(sac1)+sum(sac3)>sum(sac2)+sum(sac2):
        return("Les fausses pieces sont dans le sac 2")
    elif sum(sac2)+sum(sac3)>sum(sac3)+sum(sac3):
        return("Les fausses pieces sont dans le sac 3")
    
fauxsac= unplateau(sac1, sac2, sac3)

print(fauxsac)