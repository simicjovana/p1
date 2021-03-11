import datetime

def datum_u_untervalu(linija, od_datuma, do_datuma):
    datum = linija[3]
    if int(od_datuma[-4:]) < int(datum[-4:]):
        pass
    elif int(datum[-4:]) == int(od_datuma[-4:]) and int(od_datuma[3:5]) < int(datum[3:5]):
        pass
    elif int(datum[3:5]) == int(od_datuma[3:5]) and (int(datum[0:2]) >= int(od_datuma[0:2])):
        pass
    else: return False
    if int(do_datuma[-4:]) > int(datum[-4:]):
        pass
    elif int(datum[-4:]) == int(do_datuma[-4:]) and int(do_datuma[3:5]) > int(datum[3:5]):
        pass
    elif int(datum[3:5]) == int(do_datuma[3:5]) and (int(datum[0:2]) <= int(do_datuma[0:2])):
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






def filmovi_po_reziserima(recnik):
 #Kao parametar uzima reznik formata {'id':[naslov filma, datum, ime rezisera, zarada],,, }
 #-iz podataka pokupljenih izbacuje nepotrebne podatke(datum, id)
 #-novi kljucevi su reziseri, a vrednosti su liste u kojima su torke sa podacima zarada-film
 #vraca racnik formata {'reziser': [(zarada4,film4), (zarada2,film2), (zarada3, film3)...]...}

    podaci = {}
    for kljuc, vrednost in recnik.items():
        if vrednost[2] not in podaci.keys():                #proverava da li postoji reziser
            podaci[vrednost[2]] = [(vrednost[3],vrednost[0])]
            continue                                        #ako ne samo mu dodaje film
        else:
            podaci[vrednost[2]].append((vrednost[3], vrednost[0]))
    return podaci


def sortiranje_po_filmovima(recnik):
 #Kao parametar uzima recnik formata {'reziser': [(zarada4,film4), (zarada2,film2), (zarada3, film3)...]...}
 #-za svakog rezisera sortira filmove po zaradi neopadajuce, i bira do 3 sa najvecom zaradom
 #-dodaje ukupnu zaradu za odgovarajuce filmove svakom reziseru
 #vraca recnik formata {'reziser' : [(zarada_str1,film1),(zarada_str2,film2)...,ukupna_zarada]...}

    for reziser, filmovi in recnik.items():
        filmovi_sorted = sorted(filmovi, key= lambda film: float(film[0]), reverse=True)
        recnik[reziser] = filmovi_sorted
        while len(filmovi_sorted)> 3:
            filmovi_sorted.pop()
        ukupna_zarada = 0
        for i in range(len(filmovi_sorted)):
            ukupna_zarada += float(filmovi_sorted[i][0])
        filmovi_sorted.append(ukupna_zarada)
        recnik[reziser] = filmovi_sorted
    return recnik


def recnik_u_listu(recnik):

    #Kao parametar uzima recnik formata {'reziser' : [(zarada_str1,film1),(zarada_str2,film2)...,ukupna_zarada]...}
    #-spoji filmove u jedan string
    #-clan liste je torka u koju se dodaju reziser, do tri filma tog rezisera(sa najvecom zaradom), ukupna zarada tih filmova
    #-sortira torke po ukupnoj zaradi, prva je sa najvecom zaradom
    #vraca listu formata [(reziser,do3filma,uk_zarada)....]

    lista=[]
    for reziser,vrednosti in recnik.items():
        ukupna_zarada = vrednosti.pop()
        do_3_filma = ''
        for torka in vrednosti:
            do_3_filma += torka[1] + '|'
        do_3_filma = do_3_filma[0:-1]
        lista.append((reziser,do_3_filma,ukupna_zarada))
    lista_sorted = sorted(lista, key= lambda podaci_rezisera: float(podaci_rezisera[2]), reverse=True)
    return lista_sorted


def proveri_datum(datum):
    #proverava da li je datum korektnog formata i vrednosti
    #vraca true ako je datum ispravan

    delovi = datum.split('.')
    if len(delovi) != 3:
        return False
    if len(delovi[0]) != 2:                 #ako vrati false POLJE_GRESKA
        return False
    if len(delovi[1]) != 2:
        return False
    if len(delovi[2]) != 4:
        return False
    datum = int(delovi[0])
    mesec =int(delovi[1])
    godina = int(delovi[2])
    datum_je_ok = True
    try:
        datetime.datetime(int(godina), int(mesec), int(datum))
    except ValueError:
        datum_je_ok = False
    if not datum_je_ok:
        return False
    return True



def provera_izuzetaka(linija_lista):

    if len(linija_lista) != 6:
        raise ValueError()
    id = int(linija_lista[0])
    if linija_lista[1].strip() == '' or linija_lista[2].strip() == '' or linija_lista[4].strip()== '':
        raise Exception()
    if not proveri_datum(linija_lista[3]):
        raise Exception()
    if not linija_lista[-1][0] == '$':
        raise Exception()
    if not linija_lista[-1].strip()[-3] == '.':
        raise Exception()
    zarada = float(linija_lista[-1][1:])
    if zarada<0:
        raise Exception()





zavrsetak = False


try:
    ulazna_dat, izlazna_dat = input().split()

except ValueError:
    zavrsetak = True
    print('POLJE_GRESKA')

if zavrsetak:
    exit(0)

try:
    od_datuma = input()
    do_datuma = input()
    if (not proveri_datum(od_datuma) or not proveri_datum(do_datuma)):
        raise Exception()
    delovi = od_datuma.split('.')
    godina = int(delovi[2])
    datum = int(delovi[0])
    mesec = int(delovi[1])
    datum1 = datetime.datetime(int(godina), int(mesec), int(datum))
    delovi = do_datuma.split('.')
    godina = int(delovi[2])
    datum = int(delovi[0])
    mesec = int(delovi[1])
    datum2 = datetime.datetime(int(godina), int(mesec), int(datum))
    if datum1 > datum2:
        raise Exception()
except ValueError:
    print('KONV_GRESKA')
    zavrsetak = True
except Exception:
    print('POLJE_GRESKA')
    zavrsetak = True


if zavrsetak:
    exit(0)


obraditi = {}


#otvaranje ulazne datoteke red po red i uzimanje rezultata koji se prosledjuju funkcijama
try:
    with open(ulazna_dat,'r') as f:
        f.readline()
        for linija in f:
            if linija.strip() == '':
                continue
            linija_lista = linija.split(';')
            provera_izuzetaka(linija_lista)
            if datum_u_untervalu(linija_lista, od_datuma, do_datuma):
                kljuc = izdvajanje_id(linija_lista)
                if kljuc in obraditi.keys():
                    raise Exception()
                obraditi[kljuc]=izdvajanje_podataka(linija)
            else:
                continue


    podaci = filmovi_po_reziserima(obraditi)
    podaci_sortirano_po_filmovima = sortiranje_po_filmovima(podaci)
    podaci_sortirano_po_reziserima = recnik_u_listu(podaci_sortirano_po_filmovima)


    #otvarenja izlazne datoteke u koju se red po red izpisuju podaci u trazenom formatu
    with open(izlazna_dat,'w') as f:
        f.write('Director;Top3 Movies;Top3 Movies Revenue\n')
        for podaci_rezisera in podaci_sortirano_po_reziserima:
            f.write('{};{};{:.2f}\n'.format(podaci_rezisera[0],podaci_rezisera[1], podaci_rezisera[2]))


except ValueError as e:
    print("KONV_GRESKA")

except IOError as e:
    if 'Invalid argument' in e.args[1]:
        print('POLJE_GRESKA')
    else:
        print('DAT_GRESKA')
except Exception as e:
    print("POLJE_GRESKA")