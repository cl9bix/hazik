import random


def create_lst():
    return [random.randint(1, 100) for _ in range(30)]


def fel_1(lst):
    db = 0
    for i in lst:
        if i % 10 == 7:
            db += 1
    return db


def fel_2(lst):
    osszeg = 0
    for i in lst:
        if i % 7 != 0:
            osszeg += i
    return osszeg

def fel_3(lst):
    osszeg = 0
    db = 0
    for i in lst:
        if i % 2 == 0 and i % 3 != 0:
            osszeg += i
            db += 1
    return osszeg/db

def fel_4(lst):
    new_lst = []
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            new_lst.append(i)
    return new_lst

def main():
    lst = create_lst()
    for i in lst:
        print(i, end=' ')
    print()
    print('1.feladat:', fel_1(lst))
    print('2.feladat:', fel_2(lst))
    print('3.feladat:', fel_3(lst))
    print('4.feladat:')
    data= fel_4(lst)
    if len(data) > 0:
        for i in data:
            print(f'{i}-{i}')
    else:
        print('Nincs')


if __name__ == '__main__':
    main()
