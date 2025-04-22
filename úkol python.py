predmety = ["Matematika, Fyzika, Chemie, Biologie, Angličtina, Dějepis"]

print("Délka pole je:", len(predmety))

print("Předměty v poli:")
for predmet in predmety:
    print(predmet)

novypredmet = input("Zadej další předmět: ")
predmety.append(novypredmet)

predmety.remove("Chemie")

predmety.sort()

predmety.reverse()

print("Pole po seřazení a obrácení:")
for predmet in predmety:
    print(predmet)