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


def main():
    lst = create_list()
    print('Lista')
    for i in lst:
        print(i,end=' ')
    print()

    print('1.feladat:')
    print(get_smallest_num(lst))


if __name__ == '__main__':
    main()