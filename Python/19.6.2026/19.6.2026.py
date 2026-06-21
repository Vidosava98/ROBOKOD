#calculator
def izracunaj(izraz, prviBroj, operacija, drugiBroj):
    resenje = 0
    if operacija == ':':
        resenje = prviBroj / drugiBroj
    elif operacija == '*':
        resenje = prviBroj * drugiBroj
    elif operacija == '+':
        resenje = prviBroj + drugiBroj
    elif operacija == "-":
        resenje = prviBroj - drugiBroj

    if izraz=='' or prviBroj == '' or drugiBroj == '':
        return print("Nisi uneo validnu operaciju!")
    else:
        return print(izraz, "=", resenje)


repeat = ''
listaOperacija = ["+", "-", "*", "/"]
while repeat != 'stop':
    operacija = ''
    izraz = input("Unesi izraz: ")
    for i in listaOperacija:
        if i in izraz:
            delovi = izraz.split(i)
            operacija = i
    print("delovi: ", delovi)
    if delovi[0] != '':
        prviBroj = int(delovi[0])
    if delovi[1] != '':
        drugiBroj = int(delovi[1])
    if izraz=='' or prviBroj == '' or drugiBroj == '':
         print("Nisi uneo validnu operaciju!")
    else:
        izracunaj(izraz, prviBroj, operacija, drugiBroj)
    repeat = input("Unesi stop ukoliko zelis da iskljucis kalkulator ili continue za novi izraz.")


