def provera_datuma(linija, od_datuma, do_datuma):
    datum = linija[3]
    if int(od_datuma[-4:]) < int(datum[-4:]):
        pass
    elif int(datum[-4:]) == int(od_datuma[-4:]) and int(od_datuma[3:5]) < int(datum[3:5]):
        pass
    elif int(datum[3:5]) == int(od_datuma[-4:]) and (int(datum[0:2]) < int(od_datuma[0:2])):
        pass
    else: return False
    if int(do_datuma[-4:]) > int(datum[-4:]):
        pass
    elif int(datum[-4:]) == int(do_datuma[-4:]) and int(do_datuma[3:5]) > int(datum[3:5]):
        pass
    elif int(datum[3:5]) == int(do_datuma[-4:]) and (int(datum[0:2]) > int(do_datuma[0:2])):
        pass
    else: return False

    return True


def izdvajanje_id(linija):
    return linija[0]


def izdvajanje_podataka(linija):
    if linija[-1:] == '\n':
        linija = linija[0:-1]
    linija_lista = linija.split(';')
    return       [linija_lista[1],    linija_lista[3],    linija_lista[4],    linija_lista[5][1:]]
    #vraca listu [naslov filma,  datum,       ime rezisera,  zarada]


def izdvajanje_zarade_filmova(recnik):
    filmovi_zarada = {}
    for kljuc, vrednost in recnik.items():
        filmovi_zarada[vrednost[0]] = vrednost [3]
    return filmovi_zarada


def sortiranje_filmova(filmovi_zarada, *filmovi):
    zarade = []
    filmovi_sortirano = []
    kljucevi = list(filmovi_zarada.keys())
    vrednosti = [float(x) for x in filmovi_zarada.values()]
    for film in filmovi:
        zarade.append(float(filmovi_zarada[film]))
    zarade.sort(reverse=True)
    for zarada in zarade:
        indeks = vrednosti.index(zarada)
        film = kljucevi[indeks]
        filmovi_sortirano.append(film)
        #filmovi_sortirano.append(kljucevi[vrednosti.index(zarada)])
    while len(filmovi_sortirano) > 3:
        filmovi_sortirano.pop()
    return filmovi_sortirano



def biranje_filmova(recnik):
    podaci = {}
    for kljuc, vrednost in recnik.items():
        if vrednost[2] not in podaci.keys():                #proverava da li postoji reziser
            podaci[vrednost[2]] = [vrednost[0]]
            continue                                        #ako ne samo mu dodaje film
        else:
            podaci[vrednost[2]].append(vrednost[0])
        sortirani_filmovi = sortiranje_filmova(filmovi_zarada, *podaci[vrednost[2]])
        podaci[vrednost[2]] = sortirani_filmovi
    return podaci


def spajanje_filmova(filmovi):
    return '|'.join(filmovi)


def ukupna_zarada(filmovi_zarada, recnik):
    for kljuc, filmovi in recnik.items():
        zarada = []
        for i in range(len(filmovi)):
            zarada.append(float(filmovi_zarada[filmovi[i]]))
        recnik[kljuc] = [spajanje_filmova(filmovi), str(sum(zarada))]
    return recnik


def sortiranje_po_zaradi(recnik):
    kljucevi = list(recnik.keys())
    vrednosti = list(recnik.values())
    zarade_brojevi = []
    for i in range(len(vrednosti)):
        zarade_brojevi.append(float(vrednosti[i][1]))
    recnik_sortirano ={}
    for i in range(len(zarade_brojevi)):
        maks = max(zarade_brojevi)
        indeks = zarade_brojevi.index(maks)
        recnik_sortirano[kljucevi[indeks]] = vrednosti[indeks]
        vrednosti.pop(indeks)
        kljucevi.pop(indeks)
        zarade_brojevi.pop(indeks)
    return recnik_sortirano


ulazna_dat, izlazna_dat = input().split()
od_datuma = input()
do_datuma = input()
obraditi = {}

with open(ulazna_dat,'r') as f:
    f.readline()
    for linija in f:
        if provera_datuma(linija.split(';'), od_datuma, do_datuma):
            obraditi[izdvajanje_id(linija.split(';'))]=izdvajanje_podataka(linija)
        else:
            continue
#print(obraditi)
filmovi_zarada = izdvajanje_zarade_filmova(obraditi)
obradjeno = ukupna_zarada(filmovi_zarada, biranje_filmova(obraditi))
sortirano = sortiranje_po_zaradi(obradjeno)
#print(filmovi_zarada)
#print(obradjeno)

with open(izlazna_dat,'w') as f:
    f.write('Director;Top3 Movies;Top3 Movies Revenue\n')
    for kljuc, vrednost in sortirano.items():
        zarada = float(vrednost[1])
        f.write('{};{};{:.2f}\n'.format(kljuc,vrednost[0], zarada))