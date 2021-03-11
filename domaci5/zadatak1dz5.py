def ispravnost_godina(godina):
    if godina>0:
        return True
    raise Exception


def datum_u_upsegu(datum, godina_od,godina_do):
    godina = int(datum[6:])
    if godina>= godina_od and godina<=godina_do:
        return True
    return False



def obrada_unosa(lista):
    #uzima [id,naslov,zanrovi,datum,reziser,zarada]
    #ako je godina u opsegu pravi listu # [godina,zanrovi,zarada]
    nova_lista = [int(lista[-3][6:]), (linija_lista[2].split('|')), float(linija_lista[-1][1:])]
    return nova_lista


def obrada_podataka(lista):
    #uzima [godina,(zanrovi),zarada]
    #pravi {godina:{zanr1:zarada, zanr2:zarada...}....}
    recnik = {}
    for podlista in lista:
        godina, zanrovi, zarada = podlista
        for zanr in zanrovi:
            if godina not in recnik.keys():
                recnik[godina]= {zanr:zarada}
            else:
                recnik[godina][zanr] = recnik[godina].get(zanr,0)+zarada
    return recnik


def izdvajanje_zanra(recnik):
    #uzima {godina:{zanr1:zarada, zanr2:zarada...}....}
    #vraca [[godina,zanr,zarada_min]...]
    recnik_novo = {}
    for godina,zanrovi in recnik.items():
        for zanr, zarada in zanrovi.items():
            if godina not in recnik_novo:
                recnik_novo[godina]=[(zanr,zarada)]
            else:
                recnik_novo[godina].append((zanr,zarada))
    #recnik_novo {godina:[(zanr_min,zarada_min)...]...}
    lista = []
    for godina, zanrovi in recnik_novo.items():
        recnik_novo[godina] = sorted(zanrovi, key= lambda torka: torka[1])
    for godina, zanrovi in recnik_novo.items():
        for i in range(len(zanrovi)):
            if i == 0:
                podlista = [godina, recnik_novo[godina][i][0], recnik_novo[godina][i][1]]          #u listu dodaje godinu, zanr_min, zarada_min
                continue
            if zanrovi[i][1]==podlista[2]:
                podlista[1]= podlista[1]+'|'+zanrovi[i][0]
        lista.append(podlista)


    return lista


def sortiranje(lista):
    #uzima [(godina,zanr,zarada_min)...], vraca isto sortirano
    lista = sorted(lista, key=lambda torka:torka[0])
    return lista

try:
    dat = input().strip()
    godina_od = int(input())
    godina_do = int(input())
    if dat=='':
        raise Exception()
    if ispravnost_godina(godina_do):
        pass
    if ispravnost_godina(godina_do):
        pass
    podaci = []
    with open(dat, 'r') as f:
        prva_linija = f.readline()
        if prva_linija.strip() == '':
            raise Exception()
        for linija in f:
            linija_lista=linija.split(';')
            if datum_u_upsegu(linija_lista[-3], godina_od, godina_do):
                podaci.append(obrada_unosa(linija_lista))

    podaci_obradjeno = obrada_podataka(podaci)
    podaci_izdvojeno = izdvajanje_zanra(podaci_obradjeno)
    podaci_konacno = sortiranje(podaci_izdvojeno)
    with open('izlazZAD5.csv', 'w') as f:
        f.write('Year;Movie Genre;Genre Revenue\n')
        for l in podaci_konacno:
            f.write('{};{};{:.2f}\n'.format(l[0], l[1], l[2]))



except ValueError:
    print('KONV_GRESKA')
except IOError:
    print('DAT_GRESKA')
except Exception as e:
    print('POLJE_GRESKA')
