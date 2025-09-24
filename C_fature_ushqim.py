cmimi_njesi = float(input("Cmimi njësi (Lek): "))
sasia = int(input("Sasia (copë): "))

if sasia < 0:
    print("Sasia e pavlefshme")
else:
    karte_studenti = input("Ke kartë studenti? (po/jo): ").lower().strip()
    nenshum = cmimi_njesi * sasia

    if karte_studenti == "po":
        zbritja = nenshum * 0.10
    else:
        zbritja = 0

    totali = nenshum - zbritja

    print("------------------------------")
    print(f"Nën-total: {round(nenshum, 2)} Lek")
    print(f"Zbritja: {round(zbritja, 2)} Lek")
    print(f"Totali: {round(totali, 2)} Lek")
