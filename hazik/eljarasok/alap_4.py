import random


def create_list():
    return [random.randint(-50,50) for _ in range(10)]
    # return [6,1,3,2,8,11,5,4,7,9,10]

def num_sum(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return osszeg

def count_positive_n(lst):
    db = 0
    for i in lst:
        if i > 0:
            db += 1
    return db


def not_negative_atlag(lst):
    osszeg = 0
    # db = 0
    for i in lst:
        if i > -1:
            osszeg += i
        # db += 1
    return osszeg / len(lst)


def get_smallest_num(lst):
    masolat = lst.copy()
    masolat.sort()
    return masolat[0]

def get_sec_biggest_num(lst):
    masolat = lst.copy()
    masolat.sort(reverse=True)
    return masolat[1]

def sort_num_by_high(lst):
    masolat = lst.copy()
    masolat.sort()
    return masolat

def is_same_num(lst):
    van=False
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            van =True
            break
    if van:
        return 'Van'
    else:
        return "Nincs"

def equal_to_zero(lst):
    van = False
    for i in range(len(lst)-1):
        if lst[i] + lst[i+1] == 0:
            van = True
    if van:
        return "Van"
    else:
        return 'Nincs'


def fel_10(lst):
    db = 0
    for i in range(1,len(lst) - 1):
        if lst[i-1] > lst[i] and lst[i+1] > lst[i]:
            db += 1
    return db

def fel_11(lst):
    idx = 1
    for i in range(1,len(lst)-1):
        if lst[i-1] + lst[i+1] == lst[i]:
            idx = i
    return idx

def fel_12(lst):
    masolat = []
    for i in lst:
        if i > 0:
            masolat.append(i)

    masolat.sort()
    for i in masolat:
        print(i,end=' ')
def fel_13(lst):
    masolat = []
    for i in lst:
        if i < 0:
            masolat.append(i)

    masolat.sort(reverse=True)
    for i in masolat:
        print(i,end=' ')


def main():
    lst = create_list()
    print('Lista')
    for i in lst:
        print(i,end=' ')
    print()

    print('2.feladat:')
    print(num_sum(lst))
    print('3.feladat:')
    print(count_positive_n(lst))
    print('4.feladat:')
    print(not_negative_atlag(lst))
    print('5.feladat:')
    print(get_smallest_num(lst))
    print('6.feladat:')
    print(get_sec_biggest_num(lst))
    print('7.feladat:')
    print(sort_num_by_high(lst))
    print('8.feladat:')
    print(is_same_num(lst))
    print('9.feladat:')
    print(equal_to_zero(lst))
    print('10.feladat:')
    print(fel_10(lst))
    print('11.feladat:')
    print(fel_11(lst))
    print('12.feladat:')
    print(fel_12(lst))
    print('13.feladat:')
    print(fel_13(lst))


if __name__ == '__main__':
    main()