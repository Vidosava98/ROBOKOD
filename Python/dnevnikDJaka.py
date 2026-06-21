dnevnikUcenika = {
    "imena" : ["Milos","Vida","David", "Marko"],
    "prezimena" : ["Stanisavljevic","Arsic", "Antic", "Marinkovic"],
    "oceneMatematika": [4,5,2,4],
    "oceneSrpski": [4,4,3,5],
    "oceneLikovno": [3,5,5,5],
    "oceneIstorija": [2,4,5,5],
    "oceneGeografija": [5,4,5,4],
    "oceneEngleski": [5,5,5,5],
    "oceneFizicko":[5,5,5,5]
}

# Prvo, proverimo koliko ima učenika
brojUcenika = len(dnevnikUcenika["imena"])
print("Broj učenika:", brojUcenika)

# Za svakog učenika...
for i in range(brojUcenika):  # i ide 0,1,2,3
    # Uzmi ime i prezime učenika
    ime = dnevnikUcenika["imena"][i]
    prezime = dnevnikUcenika["prezimena"][i]
    
    
    # Saberi sve ocene za ovog učenika
    zbirOcena = 0
    brojOcena = 0
    
    # Prođi kroz sve predmete (ključeve koji počinju sa "ocene")
    for kljuc in dnevnikUcenika:
        if kljuc.startswith("ocene"):  # Ako je ovo predmet (ocene...)
            ocena = dnevnikUcenika[kljuc][i]
            if ocena == 1:
                print("Ovaj ucenik je nedovoljan")
            else:    
                zbirOcena += ocena
                brojOcena += 1
    
    # Izračunaj prosek
    prosek = zbirOcena / brojOcena
    
    print("Ucenik: ",ime, " ", prezime, " ima prosek: ", prosek)
    if prosek > 4.5:
        print(ime," ", prezime, " je odlican.")
    ## dovrsiti za sve proseke
