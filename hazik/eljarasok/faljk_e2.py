# 1. Van-e a sorozatban pozitív szám?
# 2. Hány eleme van a sorozatnak?
# 3. Mennyi a sorozatban található legkisebb szám?
# 4. Írjuk ki az első 33-mal osztható szám indexét!
# 5. Mennyi a sorozatban található számok átlagának a fele?
# 6. Igaz-e, hogy minden szám pozitív?
# 7. Hány páratlan szám található a sorozatban?
# 8. Van-e a sorozatban olyan negatív szám, amelyet újabb negatív követ?
# 9. Írjuk ki az utolsó 19-cel osztható szám indexét!
# 10. Írjuk ki a sorozatban található 5-tel osztható számokat!

def create_lst():
    return [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
            100, 67, 22, 8, -78, -6]


def fel_1(lst):
    van = False
    for i in lst:
        if i > 0:
            van = True
    return 'Van' if van == True else 'Nincs'


def fel_2(lst):
    return len(lst)


def fel_3(lst):
    masolat = lst.copy()
    masolat.sort()
    return masolat[0]


def fel_4(lst):
    for i in range(len(lst)):
        if lst[i] % 33 == 0:
            return i + 1
            break


# def fel_5(lst):
#     van= False
#     for i in lst:
#         if i < 0:
#             van = True
#     return 'Nem' if van == True else 'Igen'

def fel_5(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    atlag = osszeg / len(lst)
    return atlag / 2


def fel_6(lst):
    for i in lst:
        if i < 0:
            return False


def fel_7(lst):
    db = 0
    for i in lst:
        if i % 2 != 0:
            db += 1
    return db


def fel_8(lst):
    van = False
    for i in range(len(lst) - 1):
        if lst[i] < 0 and lst[i + 1] < 0:
            van = True
    return 'Van' if van == True else 'Nincs'

def fel_9(lst):
    for i in range(len(lst)-1,-1,-1):
        if lst[i] % 19 == 0:
            return i + 1
            break

def fel_10(lst):
    new_lst =[]
    for i in lst:
        if i % 5 ==0:
            new_lst.append(i)
    return new_lst


def main():
    lst = create_lst()
    print('1.feldat:')
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
    response = fel_6(lst)
    print('Nem igaz' if response == False else 'Igaz')
    print('7.feladat:')
    print(fel_7(lst))
    print('8.feladat:')
    print(fel_8(lst))
    print('9.feladat:')
    print(fel_9(lst))
    print('10.feladat:')
    data = fel_10(lst)
    for i in data:
        print(i,end=' ')



if __name__ == '__main__':
    main()
