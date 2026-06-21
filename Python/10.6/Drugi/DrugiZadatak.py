ukupno_baterija = int(input("Koliko ste baterija kupili? "))

dani = ukupno_baterija // 3
visak = ukupno_baterija % 3

print("Gricko ima dovoljno baterija za", dani, "celih dana.")
print("Ostaće", visak, "baterija viška.")
