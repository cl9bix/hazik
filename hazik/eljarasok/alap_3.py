def create_list():
    return [3, 6, 4, 8, 1, 9]


def fel_2(lst):
    masolat = lst.copy()
    masolat.sort(reverse=True)
    szam = 0
    for i in masolat:
        if i % 2 == 0:
            szam += i
            break
    return szam


def fel_3(lst):
    masolat = lst.copy()
    masolat.sort()
    szam = 0
    for i in masolat:
        if i % 2 == 0:
            szam += i
            break
    return szam


def is_prim(lst):
    van = False
    for i in range(len(lst)):
        db_oszto = 0
        for j in range(1, lst[i] + 1):
            if lst[i] % j == 0:
                db_oszto += 1
        if db_oszto == 2:
            van = True
    if van:
        return 'Igen'
    else:
        return 'Nem'


def fel_5(lst):
    idx = 1
    elso = 0
    for i in lst:
        if i % 2 == 0:
            elso = i
            break
        idx += 1
    return elso, idx


def fel_6(lst):
    osszeg = 0
    for i in lst:
        if i % 2 == 0:
            osszeg += i
    return osszeg


def is_first_bigger_than_last(lst):
    return 'Igen' if lst[0] > lst[-1] else 'Nem'


def main():
    lst = create_list()
    print(f'2.feladat: {fel_2(lst)}')
    print(f'3.feladat: {fel_3(lst)}')
    # print(f'4.feladat: {is_prim(lst)}')
    print('4.feladat:', is_prim(lst))
    print(f'5.feladat: Elso szam: {fel_5(lst)[0]} Indexje: {fel_5(lst)[1]}')
    print(f'6.feladat: Paros szamok osszege:', fel_6(lst))
    print('7.feladat:', fel_6(lst) / len(lst))
    print(f'8.feladat:',is_first_bigger_than_last(lst) )


if __name__ == '__main__':
    main()
