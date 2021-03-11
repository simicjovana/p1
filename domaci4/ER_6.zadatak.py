def broj_radnika():
    return int(input())


def unos_plata(n):
    return [[int(x) for x in input().split(',')] for radnik in range(n)]


def najmanja_prosecna_plata(lista,n):
    mesec = 0
    brojac = 12
    i = 0
    prosecna = 0
    while True:
        suma = 0
        for j in range(n):
            suma += lista [j][i]
        prosecna = suma / n
        if i==0 :
            min_prosecna = prosecna
            mesec = i
        if prosecna < min_prosecna:
            min_prosecna = prosecna
            mesec = i
        brojac -= 1
        i += 1
        if brojac == 0:break
    return (min_prosecna,mesec)


def izbaci(lista, broj_radnika, min_prosecna, mesec):
    najveca_plata = 0
    izbaciti = 0
    for i in range(broj_radnika):
        if lista[i][mesec] > min_prosecna and lista[i][mesec] > najveca_plata:
            najveca_plata = lista[i][mesec]
            izbaciti = i
    lista.pop(izbaciti)
    return lista


def ispis(lista):
    for podlista in lista:
        string = ''
        for j in range(len(podlista)-1):
            string += str(podlista[j]) + ','
        string += str(podlista[len(podlista)-1])
        print(string)





n = broj_radnika()
lista = unos_plata(n)

ispis(izbaci(lista, n, *najmanja_prosecna_plata(lista,n)))
