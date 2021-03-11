import re
import os

def postoji_fajl(fajl):
    if os.path.exists(fajl):
        return True
    return False


def brojanje_reci(fajl, rec):
    broj = 0
    with open(fajl,'r') as f:
        for linija in f:
            for pogodak in rec.finditer(linija):
                broj += 1
    return broj


def ispravan_fajl(fajl, broj):
    if int(fajl[6:9]) == broj:
        return True
    return False

#folder = input()
rec = 'PSIML'
trazimo_rec = re.compile(rec)
broj_ispravnih = 0
broj_ispravnih_f = 0
for i in range(1000):
    i = '{:0>3}'.format(i)
    fajl = 'PSIML_'+str(i)+'.txt'
    if postoji_fajl(fajl):
        broj_ispravnih += brojanje_reci(fajl, trazimo_rec)
        if ispravan_fajl(fajl, broj_ispravnih):
            broj_ispravnih_f +=1
            broj_ispravnih = 0

print(broj_ispravnih_f)