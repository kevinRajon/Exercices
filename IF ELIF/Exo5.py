print("Nous allons vous aider à choisir votre forfait !!!")
CONSO = float(input("Combien de temps passez vous au téléphone? "))
PRIM = (10+(0.05*CONSO))
SEC = (20+(0.02*CONSO))
if PRIM < SEC:
    print("Le forfait PRIM est le plus interessant pour vous ")
elif SEC < PRIM:
    print("Le forfait SEC est le plus interessant pour vous ")
else:
    print("Les deux frofaits sont equivalents ")
