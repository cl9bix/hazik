import random


def create_list():
    return [random.randint(-50, 50) for _ in range(40)]


def kiir(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    altag = osszeg / len(lst)
    return osszeg, altag


def fel_4(lst):
    db = 0
    for i in lst:
        if i < 0:
            db += 1
    return db


def fel_5(lst):
    db = 0
    osszeg = 0
    for i in lst:
        if i > 0:
            db += 1
            osszeg += i
    return osszeg / db


def fel_6(lst):
    db = 0
    for i in range(len(lst) - 1):
        if lst[i] < 0 and lst[i + 1] > 0:
            db += 1
    return db


def fel_7(lst):
    db = 0
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            db += 1
    return db


def fel_8(lst):
    db = 0
    for i in lst:
        if i == 0:
            db += 1
    return db


import math


def fel_9(lst):
    new_lst = []
    for i in lst:
        if i > 0:
            sqrt_i = math.isqrt(i)
            if sqrt_i * sqrt_i == i:
                new_lst.append(i)
    return new_lst


def only_negative(lst):
    new_lst = []
    for i in lst:
        if i < 0:
            new_lst.append(i)
    new_lst.sort(reverse=True)
    print(new_lst)


def main():
    lst = create_list()
    for i in lst:
        print(i, end=' ')
    print()
    print(f'2.feladat:')
    print('Osszeg:', kiir(lst)[0])
    print('3.feladat:\nAtlag:', kiir(lst)[1])
    print('4.feladat:\n', fel_4(lst), 'db negativ szam van')
    print('5.feladat:\nPozitiv szamok atlaga:', fel_5(lst))
    print('6.feladat:\n', fel_6(lst), 'db')
    print('7.feladat:\n', fel_7(lst), 'db')
    print('8.feladat:\n', fel_8(lst), 'db')
    print('9.feladat:')
    fel_9_lst = fel_9(lst)
    for i in fel_9_lst:
        print(i, end=' ')

    print(fel_9_lst)
    only_negative(lst)


if __name__ == '__main__':
    main()
