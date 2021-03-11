def obrada_ulaza(lista):
    # uzima [id, naslov, zanrovi, datum, reziser, zarada]
    # vraca [(reziser, zanr1), (reziser, zanr2)...]
    zanrovi = lista[2].split('|')           #[zanr1,zanr2,zanr3..]
    lista_obradjeno = []
    for i in range(len(zanrovi)):
        zanr = zanrovi[i]
        lista_obradjeno.append((lista[-2],zanr))
    return lista_obradjeno


def po_reziserima(lista,zanrovi_od_interesa):
    #uzima vraca [[(reziser, zanr1), (reziser, zanr2)...]...]
    #vraca {reziser1: {zanr1:broj, zanr2:broj...}...}
    recnik = {}
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            reziser = lista[i][j][0]
            zanr = lista[i][j][1]
            if zanr in zanrovi_od_interesa:
                if reziser not in recnik.keys():
                    recnik[reziser]={zanr:1}
                else:
                    recnik[reziser][zanr]= recnik[reziser].get(zanr,0)+1
        if lista[i][0][0] not in recnik.keys():
            recnik[lista[i][0][0]]={zanrovi_od_interesa[0]:0}
    return recnik


def sortiranje_zanrova(recnik, zanrovi_od_interesa):
    #uzima {reziser1: {zanr1:broj, zanr2:broj...}...}
    #vraca {reziser : [(zanr1 , broj),(zanr2 , broj)]...}
    recnik_novo = {}
    for reziser,zanrovi in recnik.items():
        for zanr_od_interesa in zanrovi_od_interesa:
            if zanr_od_interesa not in zanrovi.keys():
                recnik[reziser][zanr_od_interesa] = 0

        for zanr,broj in zanrovi.items():
            if reziser not in recnik_novo.keys():
                recnik_novo[reziser] = [(zanr,broj)]
            else:
                recnik_novo[reziser].append((zanr,broj))

    for reziser,zanrovi in recnik_novo.items():
        recnik_novo[reziser]=sorted(zanrovi,key= lambda  torka : torka[0])
    return recnik_novo


def obrada_ispis(recnik):
    #uzima {reziser : [(zanr1 , broj),(zanr2 , broj)]...}
    #vraca [[reziser, zanr1 : broj|zanr2 : broj]...]
    lista = []
    for reziser, zanrovi in recnik.items():
        string = ''
        for i in range(len(zanrovi)):
            if i==0:
                string += zanrovi[i][0] + ' : '+str(zanrovi[i][1])
            else:
                string += '|'+zanrovi[i][0] + ' : ' + str(zanrovi[i][1])
        lista.append([reziser,string])
    return lista


try:
    #dat = input().strip()
    #zanrovi_od_interesa = input().split(',')
    #if dat=='':
    #    raise Exception()
    zanrovi_od_interesa = ['Romance','Drama','Mystery']
    if len(zanrovi_od_interesa)==1 and len(zanrovi_od_interesa[0])==0:
        raise Exception()

    podaci = []
    with open('pp1_movies_20201.csv', 'r') as f:
        prvi_red = f.readline().strip()
        if prvi_red=='':
            raise Exception()
        for linija in f:
            linija_lista = linija.split(';')
            podaci.append(obrada_ulaza(linija_lista))

    recnik_obradjeno = po_reziserima(podaci,zanrovi_od_interesa)
    recnik_sortirano = sortiranje_zanrova(recnik_obradjeno, zanrovi_od_interesa)
    lista_za_ispis = obrada_ispis(recnik_sortirano)

    with open('izlazZAD5_2.csv','w') as f:
        f.write('Director;Movie Genre Count\n')
        for l in lista_za_ispis:
            f.write('{};{}\n'.format(l[0],l[1]))



except IOError:
    print('DAT_GRESKA')
except Exception as e:
    print('POLJE_GRESKA')
