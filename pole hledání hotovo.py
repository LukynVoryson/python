cisla = [3, 7, 1, 9, 4, 2, 8]

hledane_cislo = int(input("Zadej číslo, které chceš v poli najít: "))

nalezeno = False

for i in range(len(cisla)):
    if cisla[i] == hledane_cislo:
        print("Našel jsem tuto hodnotu na pozici", i, "!")
        nalezeno = True
        break

if not nalezeno:
    print("Zadaná hodnota tady není.")
