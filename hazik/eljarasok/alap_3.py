def create_list():
    return [3, 6, 4, 8, 1, 9]


def fel_2(lst):
    lst.sort(reverse=True)
    szam = 0
    for i in lst:
        if i % 2 == 0:
            szam += i
            break
    return szam


def fel_3(lst):
    lst.sort()
    szam = 0
    for i in lst:
        if i % 2 == 0:
            szam += i
            break
    return szam


def is_prim(lst):
    van = False
    for i in range(1, len(lst)):
        db_oszto = 0

        for j in range(1, i + 1):
            if lst[i] % j == 0:
                db_oszto += 1
        # if db_oszto == 2:
        #     van = True
        #     break
    # if van:
    #     return 'Van'
    # else:
    #     return 'Nincs'


def main():
    lst = create_list()
    print(f'2.feladat: {fel_2(lst)}')
    print(f'3.feladat: {fel_3(lst)}')
    print(f'4.feladat: {is_prim(lst)}')


if __name__ == '__main__':
    main()
