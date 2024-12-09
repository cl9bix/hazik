class Data:
    def __init__(self, sor):
        self.date = sor.split(';')[0]
        self.benzin = int(sor.split(';')[1])
        self.gazolaj = int(sor.split(';')[2])


def create_lst():
    lst = []
    with open(file='uzemanyag.txt', mode='r', encoding='utf-8') as f:
        for i in f:
            obj = Data(i)
            lst.append(obj)
    return lst


def fel_4(lst):
    legkisebb = lst[0].benzin - lst[0].gazolaj
    for i in lst:
        if (i.benzin - i.gazolaj) >= 0 and (i.benzin - i.gazolaj) < legkisebb:
            legkisebb = i.benzin - i.gazolaj
    return legkisebb


def fel_5(lst):
    lgk = fel_4(lst)
    db = 0
    for i in lst:
        if i.benzin - i.gazolaj == lgk or i.gazolaj - i.benzin == lgk:
            db += 1
    return db


def fel_6(lst):
    van = False
    for i in lst:
        if int(i.date.split('.')[0]) % 4 == 0 and int(i.date.split('.')[2]) == 24:
            van = True
            break
    return 'Volt valtozas szokonapon' if van == True else 'Nem volt valtozas szokonapon'


def fel_7(lst):
    for i in lst:
        with open(file='euro.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{i.date};{round(i.benzin / 307.7, 2)};{round(i.gazolaj / 307.7, 2)}\n')


def fel_8(lst):
    user_year = int(input('Kerem adja meg az evszamot [2011..2016]: '))
    while True:
        if user_year < 2011 or user_year > 2016:
            user_year = int(input('Kerem adja meg az evszamot [2011..2016]: '))
        else:
            return user_year
            return False


def fel_9(lst,valt1,valt2):
    napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in lst:
        if int(i.date.split('.')[0]) % 4 == 0:
            csere = 28
            if csere in napok:
                idx = napok.index(csere)
                napok[idx] = 29
    # valt1_ev = valt1.date.split('.')[0]
    # valt1_honap = valt1.date.split('.')[1]
    # valt1_nap = valt1.date.split('.')[2]
    #
    # valt2_ev = valt2.date.split('.')[0]
    # valt2_honap = valt2.date.split('.')[1]
    # valt2_nap = valt2.date.split('.')[2]

    valt1_ev,valt1_honap,valt1_nap = map(int,valt1.date.split('.'))
    valt2_ev,valt2_honap,valt2_nap = map(int,valt2.date.split('.'))

    if valt1_honap == valt2_honap:
        return valt2_nap - valt1_nap

    elif valt2_honap == valt1_honap + 1:
        return napok[valt1_honap - 1] - valt1_nap + valt2_nap


def fel_10(lst,user_year):
    year_changes = [x for x in lst if int(x.date.split('.')[0]) == user_year]

    max_gap = 0
    for i in range(len(year_changes) - 1):
        gap = fel_9(year_changes, year_changes[i], year_changes[i + 1])
        if gap > max_gap:
            max_gap = gap

    return f'10. feladat: A leghosszabb idokulonbseg a(z) {user_year} evben: {max_gap} nap'



def main():
    lst = create_lst()
    print(f'3. feladat: Valtozasok szama: {len(lst)}')
    print(f'4. feladat: A legkisebb kulonbseg: {fel_4(lst)}')
    print(f'5. feladat: A legkisebb kulonbseg elofordulasa: {fel_5(lst)}')
    print(f'6. feladat: {fel_6(lst)}')
    fel_7(lst)
    fel_8(lst)
    fel_10(lst,user_year=fel_8(lst))


if __name__ == '__main__':
    main()
