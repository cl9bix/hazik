def create_lst():
    return [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
            100, 67, 22, 8, -78, -6]


def fel_1(lst):
    van = False
    for i in lst:
        if i % 100 == 0:
            van = True
    return 'Igen' if van == True else 'Nem'


def fel_2(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 7 == 0:
            return i + 1
            break


def fel_3(lst):
    for i in range(len(lst)):
        if lst[i] % 19 == 0:
            return i + 1


def fel_4(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return (len(lst) / osszeg) ** 2


def fel_5(lst):
    van = False
    for i in lst:
        if i < 10:
            van = True
    return 'Nem' if van == True else 'Igaz'


def fel_6(lst):
    db = 0
    for i in lst:
        if i % 9 == 0:
            db += 1
    return db

def fel_7(lst):
    new_lst=[]
    for i in lst:
        if i % 15 == 0:
            new_lst.append(i/2)
    return new_lst


def fel_9(lst):
    van=False
    for i in range(len(lst)-1):
        if lst[i] < 0 and lst[i+1] > 0:
            van=True
    return 'Van' if van == True else False

def fel_10(lst):
    masolat = lst.copy()
    masolat.sort()
    return masolat[0] / 2


def main():
    lst = create_lst()
    print('1.feladat:')
    print(fel_1(lst))
    print('2.feladat:')
    print(fel_2(lst))
    print('3.feladat:')
    print(fel_3(lst))
    print('4.feladat:')
    print(fel_4(lst))
    print('5.feladat:')
    print(fel_5(lst))
    print('6.feladat:')
    print(fel_6(lst))
    print('7.feladat:')
    hetes = fel_7(lst)
    for i in hetes:
        print(i,end=' ')
    print()
    print('8.feladat:')
    print(len(lst))
    print('9.feladat:')
    print(fel_9(lst))
    print('10.feladat:')
    print(fel_10(lst))



if __name__ == '__main__':
    main()
