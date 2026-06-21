# Dictionary  jeste  tip podataka koji sluzi za skladistenje podataka
# tipa
#   "kljuc" : "vrednost"

mojDnevnik = {
    "ime": "Vida",
    "prezime": "Arsic",
    "godiste": "1998",
}

## stampanje celog dictionary-ija

print("Svi podaci mog dictionary-a: ", mojDnevnik)


## stampanje podataka pojedinacnio

for (key, value) in mojDnevnik.items():
    print("Ovo je", key, "iz mog dictionary-a: ", value)


## stampanje  odredjene vrednosti iz Dictionary-ija

print("Moje ime je ", mojDnevnik["ime"])
    
## vrednosti u Dictionary-ima jesu  promenljive
    
mojDnevnik["ime"] = "Vidosava"


## dodavanje vrednosti u dictionary

mojDnevnik["eyeColor"] = "blue"


## stampanje celog dictionary-ija

print("Svi podaci mog dictionary-a: ", mojDnevnik)
