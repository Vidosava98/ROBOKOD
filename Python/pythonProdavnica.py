proizvodi = ["Hleb", "Mleko", "Čokolada"]
cene = [50, 90, 120]

ukupno = 0

print("Dobrodošli u prodavnicu!")
for i in range(len(proizvodi)):
    print(i + 1, "-", proizvodi[i], "(", cene[i], "din)")

print("0 - Kraj kupovine")

while True:
    izbor = int(input("Izaberite proizvod (1-3): "))

    if izbor == 0:
        break
    elif 1 <= izbor <= len(proizvodi):
        ukupno += cene[izbor - 1]
        print("Dodali ste", proizvodi[izbor - 1])
    else:
        print("Pogrešan izbor.")

print("Ukupan iznos za plaćanje je:", ukupno, "dinara.")
