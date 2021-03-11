def racunanje(string):
    rez = ''
    eksponent_pozicija = 0
    preskoci = False
    for i in range(len(string)):
        if i==0:
            while string[i].isdigit():
                rez += string[i]
            rezultat = int(rez)
            rez = ''
        if string[i] == '+':
            pass
        elif string[i] == '*':
            pass
        elif string[i] == 'e':
            continue
        elif string[i] == 'x':
            continue
        elif string[i] == 'p':
            rez = string[i+1]

        else:
            rez += string[i]

    return rezultat





def radi():
    try:
        string = input().strip()
        for slovo in string:
            if slovo == 'e' or slovo == 'x' or slovo == 'p' or slovo == '+' or slovo == '*':
                pass
            else:
                broj = int(slovo)
        vrednost = racunanje(string)

    except ValueError:
        print('uneta je pogresna vrednst')










radi()






