robokodUcenici = ["Ognjen", "Vasa", "Masa", "Mila", "Tadija"]
robokodUcenici.append("Lazar")
print(robokodUcenici)

del robokodUcenici[0]
print(robokodUcenici)

robokodUcenici.append("Ognjen")
robokodUcenici.insert(0, "Vuk")

print("\n Trenutna lista ucenika u robokodu:",robokodUcenici)

for brojac in range(0,len(robokodUcenici)):
     print(brojac+1 ,robokodUcenici[brojac])

listaSort = sorted(robokodUcenici)
print(listaSort)

listaSort.reverse()
print(listaSort)
