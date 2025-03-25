#uživatel tohoto programu je doktor, který chce přidávat pacienty do svojí databáze
#uprav kód pomocí cyklu tak, aby se program nejdřív zeptal uživatele kolik pacientů chce přidat a podle toho pak proběhl kód níže


#tento kousek kódu se bude opakovat tolikrát kolikrát zadá uživatel
pocet = int(input("Kolik pacientů chcete přidat? "))
i=()
for i in range (pocet):

    jmeno = input("Zadejte jméno pacienta, kterého chcete přidat")
    prijmeni = input("Zadejte příjmení pacienta, kterého chcete přidat")
    rok = int(input("Zadejte rok narození pacienta ktetého chcete přidat"))
    print(f"Pacient {jmeno} {prijmeni} rok narození {rok} byl přidán")git remote add origin https://github.com/LukynVoryson/cvi-en-.git
git branch -M main
git push -u origin main