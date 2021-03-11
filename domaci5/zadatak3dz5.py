import datetime

def provera_datuma(datum):
    dan = datum[:2]
    mesec = datum[3:5]
    godina = datum[-4:]
    if len(datum.split('.'))!=3:
        raise Exception()
    if len(godina)!= 4:
        raise Exception()
    if len(dan)!= 2:
        raise Exception()
    if len(mesec)!= 2:
        raise Exception()

    datetime.datetime(int(godina),int(mesec),int(dan))

    return True


def datum_u_opsegu(datum,od_datum,do_datum):
    dan = int(datum[:2])
    mesec = int(datum[3:5])
    godina = int(datum[-4:])
    dan_od = int(od_datum[:2])
    mesec_od = int(od_datum[3:5])
    godina_od = int(od_datum[-4:])
    dan_do = int(do_datum[:2])
    mesec_do = int(do_datum[3:5])
    godina_do = int(do_datum[-4:])
    if datetime.datetime(godina,mesec,dan) <= datetime.datetime(godina_do,mesec_do,dan_do) and datetime.datetime(godina,mesec,dan)>=datetime.datetime(godina_od,mesec_od,dan_od):
        return True
    return False


def zanr_izbor(zanr,lista):
    zanrovi = lista.split('|')
    if zanr in zanrovi:
        return True
    return False


def obrada_ulaza(linija_lista):
    # uzima [id,naslov,zanrovi, datum,reziser,zarada]
    #vraca [reziser,film,zarada_float]
    return [linija_lista[-2],linija_lista[1],float(linija_lista[-1][1:])]

def po_reziseru(lista):
    #uzima [reziser,film,zarada_float]
    #vraca {reziser: [(film2,zarada2),(film1,zarada1),(film3,zarada3)..]....}
    recnik = {}
    for linija in lista:
        reziser = linija[0]
        film = linija[1]
        zarada = linija[2]
        if reziser not in recnik.keys():
            recnik[reziser] = [(film,zarada)]
        else:
            recnik[reziser].append((film,zarada))
    return recnik


def sortiranje(recnik):
    #uzima {reziser: [(film2,zarada2),(film1,zarada1),(film3,zarada3)..]....}
    #vraca {reziser: [(filmmin,zaradamin),(filmmax,zaradamax)]....}
    recnik_novo = {}
    for reziser,filmovi in recnik.items():
        recnik[reziser]=sorted(filmovi,key= lambda torka: torka[1])
    for reziser,filmovi in recnik.items():
        recnik[reziser] = [filmovi[0],filmovi[-1]]

    return recnik


def obrada_ispis(recnik):
    #uzima {reziser: [(filmmin,zaradamin),(filmmax,zaradamax)]....}
    #vraca [(reziser,filmmin : zarada, filmmax : zarada),..]
    lista = []
    for reziser, filmovi in recnik.items():
        film_min,zarada_min = filmovi[0]
        film_max,zarada_max = filmovi[1]
        lista.append((reziser,film_min,zarada_min,film_max,zarada_max))
    lista = sorted(lista,key= lambda torka:torka[0])

    return lista


try:
    dat = input().strip()
    od_datuma= input().strip()
    do_datuma = input().strip()
    zanr = input().strip()
    #dat = 'ulaz3.csv'
    #od_datuma= '01.01.2000'
    #do_datuma = '18.12.2020'
    #zanr = 'Drama'
    if not provera_datuma(od_datuma):
        raise Exception()
    if not provera_datuma(do_datuma):
        raise Exception()
    podaci = []

    with open('pp1_movies_20201.csv','r') as f:
        prva_linija = f.readline().strip()
        if prva_linija =='':
            raise Exception
        for linija in f:
            linija_lista = linija.strip().split(';')
            if not provera_datuma(linija_lista[-3]):
                raise Exception
            if datum_u_opsegu(linija_lista[-3],od_datuma,do_datuma) and zanr_izbor(zanr,linija_lista[2]):
                podaci.append(obrada_ulaza(linija_lista))

    recnik_filmovi_svi = po_reziseru(podaci)
    sortiran_recnik = sortiranje(recnik_filmovi_svi)
    lista_ispis = obrada_ispis(sortiran_recnik)

    with open('izlaz.csv','w') as f:
        f.write('Director;Movie Title Min Revenue;Movie Title Max Revenue\n')
        for l in lista_ispis:
            f.write('{};{} : {};{} : {}\n'.format(l[0],l[1],l[2],l[3],l[4]))




# [id,naslov,zanrovi, datum,reziser,zarada]

except ValueError:
    print('KOVN_GRESKA')
except IOError:
    print('DAT_GRESKA')
except Exception as e:
    print('POLJE_GRESKA')