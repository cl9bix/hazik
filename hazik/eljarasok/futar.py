import random


def create_lst():
    return [random.randint(1, 20) for _ in range(10)]


def fel_1(lst):
    for i in lst:
        if i <= 3:
            print(f'{i}km - 500ft')
        elif i <= 7:
            print(f'{i}km - 700ft')
        elif i <= 11:
            print(f'{i}km - 900ft')
        elif i <= 15:
            print(f'{i}km - 1400ft')
        elif i <= 20:
            print(f'{i}km - 2000')


def fel_2(lst):
    osszesen = 0
    for i in lst:
        if i <= 3:
            osszesen += 500
        elif i <= 7:
            osszesen += 700
        elif i <= 11:
            osszesen += 900
        elif i <= 15:
            osszesen += 1400
        elif i <= 20:
            osszesen += 2000
    return osszesen


def fel_4(lst):
    ut1 = 0
    ut2 = 0
    ut3 = 0
    ut4 = 0
    ut5 = 0
    for i in lst:
        if i <= 3:
            ut1 += 1
        elif i <= 7:
            ut2 += 1
        elif i <= 11:
            ut3 += 1
        elif i <= 15:
            ut4 += 1
        elif i <= 20:
            ut5 += 1
    return (ut1, ut2, ut3, ut4, ut5)


def fel_5(lst):
    lst = [i for i in fel_4(lst)]
    masolat = lst.copy()
    masolat.sort(reverse=True)
    return lst.index(masolat[0]) + 1


def is_n(lst, n):
    return f"Szerepel {n}" if n in lst else f"Nem szerepel {n}"


def fel_7(lst):
    new_lst = []
    for i in lst:
        if i > 5 and i < 11:
            new_lst.append(i)

    return new_lst


def fel_8(new_lst):
    osszeg = 0
    for i in new_lst:
        osszeg += i
    if osszeg == 0:
        return
    return osszeg / len(new_lst)


def fel_9(lst):
    masolat = lst.copy()
    masolat.sort(reverse=True)
    return lst.index(masolat[0]) + 1, masolat[0]


def fel_10(lst):
    masolat = lst.copy()
    masolat.sort()
    return lst.index(masolat[0]) + 1, masolat[0]


def fel_11(lst):
    van = False
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            van = True
            break
    return 'Van' if van == True else "Nincs"


def main():
    lst = create_lst()
    for i in lst:
        print(i, end=' ')
    print()
    print('1.feladat:')
    fel_1(lst)
    print('2.feladat:')
    print(fel_2(lst), 'ft')
    print('3.feladat:')
    print(fel_2(lst) / len(lst))
    print('4.feladat:')
    for i in range(0, 5):
        print(f'Az ut_{i + 1} - {fel_4(lst)[i]}szor fordul elo')
    print()

    print('5.feladat:')
    print(f'Az Ut_{fel_5(lst)}')
    print('6.feladat:')
    print(is_n(lst, n=15))
    print('7.feladat:')
    print(fel_7(lst))

    print('8.feladat:')
    print(fel_8(fel_7(lst)))

    print('9.feladat:')
    print(f'{fel_9(lst)[1]} a leghosszabb ut es {fel_9(lst)[0]}. tette meg')

    print('10.feladat:')
    print(f'{fel_10(lst)[1]} a legrovidebb ut es {fel_10(lst)[0]}. tette meg')

    print('11.feladat:')
    print(fel_11(lst))


if __name__ == '__main__':
    main()
