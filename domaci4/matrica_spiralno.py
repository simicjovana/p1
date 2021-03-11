def unos_stringa():
    return input()


def korektan_unos(string):                    #ispituje da li je unos korektan
    for slovo in string:
        if not slovo.isdigit():
            return False
    return True


def deljiv(broj):               #ispituje da li je broj deljiv sa 12
    zbir_cifara = 0
    for cifra in range(len(broj)):
        zbir_cifara += int(broj[cifra])
    if zbir_cifara % 3 != 0:
        return False
    if int(broj[-2:]) % 4 != 0:
        return False
    return True


def obrada(broj):
    deljivi = []                                #brojevi deljivi
    pozicije = []                               #njihove pozicije
    for i in range(len(broj)):
        for j in range(i+1,len(broj)+1):
            if deljiv(broj[i:j]):
                if len(broj[i:j]) > 1 and broj[i] =='0':
                    continue
                elif len(broj[i:j]) == 1 and broj[i] =='0':
                    deljivi.append(broj[i:j])
                    pozicije.append(i)
                elif len(broj[i:j]) > 1 and broj[i] != '0':
                    deljivi.append(broj[i:j])
                    pozicije.append(i)
    return (deljivi, pozicije)


def ispis_deljivih(deljivi,pozicije):
    for i in range(len(deljivi)):
        print('Broj {} na poziciji {}'.format(deljivi[i],pozicije[i]))


broj = unos_stringa()
if korektan_unos(broj):
    ispis_deljivih(*obrada(broj))
#elif broj == ' ':

else:
    print('', end = '')

