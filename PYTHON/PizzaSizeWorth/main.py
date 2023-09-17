SrednicaPizzy=float(input("Podaj Srednice Pizzy: "))
PolePizzy=float(SrednicaPizzy/2 * SrednicaPizzy/2 *3.14)
CenaPizzy=float(input("Podaj Cene Pizzy: "))
CenaPizzyZaCm2=float(CenaPizzy/PolePizzy)

print("Cena za cm^2 pizzy za "+str(CenaPizzy)+" o srednicy "+str(SrednicaPizzy)+" wynosi: "+str(CenaPizzyZaCm2))