ucenici = []

while True:
    print("\n1. Dodaj 2. Ispiši listu 3. Najbolji 4. Izlaz")
    izbor = input("Izbor: ")
    
    if izbor == "1":
        ime = input("Ime: ")
        razred = input("Razred: ")
        prosek = float(input("Prosek (1-5): "))
        ucenici.append((ime, razred, prosek))  # dodajemo tuple
        print("Dodao si uspesno!")
        
    elif izbor == "2":
        if not ucenici:
            print("Nema učenika.")
        else:
            i = 0
            for ucenik in ucenici:
                ime = ucenik[0]
                razred = ucenik[1]
                prosek = ucenik[2]
                print("", i, ". ", ime,  "(", razred, ") - ", prosek)
                i = i + 1
                
    elif izbor == "3":
        if ucenici:
            naj = max(ucenici, key=lambda x: x[2])
            print("Najbolji: ", naj[0]," (", naj[1], ") - ", naj[2])
        else:
            print("Nema učenika.")
            
    elif izbor == "4":
        print("Doviđenja!")
        break
    else:
        print("Pogrešan unos.")
