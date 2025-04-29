skore = []

for i in range(10):
    bod = int(input(f"Zadej skóre hráče {i+1} (0-60): "))
    skore.append(bod)

print("Skóre hráčů:", skore)

prumer = sum(skore) / len(skore)
print("Průměrné skóre:", prumer)

print("Nejvyšší skóre:", max(skore))
print("Nejnižší skóre:", min(skore))

vysoke_skore = 0
for bod in skore:
    if bod > 50:
        vysoke_skore += 1

if vysoke_skore > 5:
    print("Výborný výkon!")
else:
    print("Můžete to příště zkusit lépe.")