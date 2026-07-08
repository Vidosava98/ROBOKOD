

filmovi = {
    "1": {"naziv": "Avatar 2", "cena": 500},
    "2": {"naziv": "Spajdermen", "cena": 450},
    "3": {"naziv": "Minecraft film", "cena": 400}
}

racun = []


def prikazi_filmove():
    print("\n FILMOVI NA REPERTOARU")
    print("-----------------------")

    for broj, film in filmovi.items():
        print(broj, "-", film["naziv"], "-", film["cena"], "din")


def kupi_kartu():
    prikazi_filmove()

    izbor = input("\nIzaberi film (1-3): ")

    if izbor in filmovi:
        broj_karata = int(input("Koliko karata želiš? "))

        film = filmovi[izbor]

        ukupno = broj_karata * film["cena"]

        kupovina = {
            "film": film["naziv"],
            "karte": broj_karata,
            "cena": ukupno
        }

        racun.append(kupovina)

        print("\nUspešna kupovina!")
        print("Film:", film["naziv"])
        print("Broj karata:", broj_karata)
        print("Cena:", ukupno, "din")

    else:
        print("Film ne postoji!")


def prikazi_racun():
    if len(racun) == 0:
        print("\nRačun je prazan.")
        return

    print("\n===================")
    print("       RAČUN")
    print("===================")

    ukupna_cena = 0

    for stavka in racun:
        print("\nFilm:", stavka["film"])
        print("Broj karata:", stavka["karte"])
        print("Cena:", stavka["cena"], "din")

        ukupna_cena += stavka["cena"]

    print("-------------------")
    print("UKUPNO:", ukupna_cena, "din")
    print("===================")


def meni():

    while True:

        print("""
==================== BIOSKOP ====================
1. Prikaži filmove
2. Kupi kartu
3. Prikaži račun
4. Izlaz
""")

        izbor = input("Izaberi opciju: ")

        if izbor == "1":
            prikazi_filmove()

        elif izbor == "2":
            kupi_kartu()

        elif izbor == "3":
            prikazi_racun()

        elif izbor == "4":
            print("Hvala što ste posetili bioskop! ")
            break

        else:
            print("Pogrešan izbor!")


meni()
