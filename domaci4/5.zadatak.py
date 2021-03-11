def unos_teksta():
    return input()


def da_li_obraditi(rec):
    rec = rec.lower()
    if rec[0] == rec[-1]:
        return True
    return False


def obrada_reci(rec):
    rec = rec.lower()
    while len(rec) >= 3 :
        if da_li_obraditi(rec):
            rec = rec[1:-1]
        else: break
    return rec


def izbacivanje_slova(recenica,zameniti,zamena):
    i = recenica.index(zameniti)
    j = i + len(zameniti)
    nova_recenica = recenica[:i] + zamena + recenica[j:]
    return nova_recenica


def obrada_recenice(recenica):
    reci = []
    rec = ''
    recenica_novo = recenica[:]
    for znak in recenica:
        if znak.isalpha():
            rec += znak
        else:
            if len(rec) >= 3:
                reci.append(rec)
            rec = ''
    for i in range(len(recenica)):
        for j in range(i+3,len(recenica)+1):
            if recenica[i:j] in reci and da_li_obraditi(recenica[i:j]):
                zameniti = recenica[i:j]
                zamena = obrada_reci(recenica[i:j])
                recenica_novo = izbacivanje_slova(recenica_novo,zameniti,zamena)
                #recenica_novo.replace(recenica[i:j], obrada_reci(recenica[i:j]))
    return recenica_novo




print(obrada_recenice(unos_teksta()))

