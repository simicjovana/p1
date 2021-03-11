def korektan_unos(br1, br2):
    znak = ('+', '-')
    if (not br1[0].isdigit and br1[0] not in znak) or (br1[0].isdigit() and br1[0] == '0'):
        return False
    if (not br2[0].isdigit and br2[0] not in znak) or (br2[0].isdigit() and br2[0] == '0'):
        return False
    for i in range(1, len(br1)):
        if not br1[i].isdigit:
            return False
    for i in range(1, len(br2)):
        if not br2[i].isdigit:
            return False
    return True


def da_li_je_sabiranje(broj1, broj2):
    if broj1[0] == '-' or broj2[0] == '-':
        return False
    return True


def sabiranje(br1, br2):
    zbir = ''
    prelaz = 0
    brojac = 0
    if len(br2) > len(br1):
        br1, br2 = br2, br1
    indeks = len(br1) - 1

    for i in range(len(br2) - 1, -1, -1):
        if br2[i].isdigit():
            pom = int(br1[indeks]) + int(br2[i]) + prelaz
            if pom > 9:
                prelaz = 1
                pom -= 10
            else:
                prelaz = 0
            zbir = str(pom) + zbir
            brojac += 1
        indeks -= 1
    brojac = len(br1) - brojac - 1

    if brojac == -1 and prelaz == 1:
        zbir = '1' + zbir
    while brojac > -1 and br1[brojac].isdigit():
        pom = int(br1[brojac]) + prelaz
        if pom > 9:
            prelaz = 1
            pom -= 10
        else:
            prelaz = 0
        zbir = str(pom) + zbir
        brojac -= 1
    if brojac == -1 and prelaz == 1:
        zbir = '1' + zbir

    return zbir


def oduzimanje(br1, br2):
    razlika = 0
    return razlika


def ispis(broj):
    print('Rezultat je {}'.format(broj))


broj1 = input()
broj2 = input()
if korektan_unos(broj1, broj2):
    if da_li_je_sabiranje(broj1, broj2):
        ispis(sabiranje(broj1, broj2))
    else:
        ispis(oduzimanje(broj1, broj2))
else:
    print('')

