#na konci tohoto kódu se zeptej uživatele, zda chce kód opakovat, pokud ano, tak celý kód opakuj
#takto to dělej dokud uživatel nezadá, že chce aby program skončil
opakovat="ano"
while(opakovat=="ano"):
    print("Co by si potřeboval?")
    print("1. vypočítat součet")
    print("2. vypočítat rozdíl")
    print("3. vypočítat násobek")
    akce = int(input("Zadejte číslo akce kterou chcete provést"))
    if(akce==1):
        cislo1=int(input("Zadejte první číslo "))
        cislo2=int(input("Zadejte první číslo "))
        print(cislo1+cislo2)
    elif(akce==2):
        cislo1=int(input("Zadejte první číslo "))
        cislo2=int(input("Zadejte první číslo "))
        print(cislo1-cislo2)
    elif(akce==3):
        cislo1=int(input("Zadejte první číslo "))
        cislo2=int(input("Zadejte první číslo "))
        print(cislo1*cislo2)
    else:
        print("Zadal jsi špatnou akci")

    opakovat = input("chcete kód zopakovat")