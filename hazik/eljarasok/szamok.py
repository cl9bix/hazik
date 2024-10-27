# 1. Írjuk ki a sorozatban található utolsó köbszámot!
# 2. Hány eleme van a sorozatnak?
# 3. Mennyi a sorozatban található számok közti diferencia összege?
# 4. Van-e a sorozatban olyan szám, amely osztható az indexével?
# 5. Igaz-e, hogy a sorozat egy számtani sorozat? !!!!!!!
# 6. Írjuk ki a sorozatban található első négyzetszám négyzetét!
# 7. Van-e a sorozatban prímszám?
# 8. Igaz-e, hogy minden szám (-50,50) nyílt intervallumba esik?
# 9. Írjuk ki a sorozatban található prímszámokat!
# 10. Mennyi a sorozatban található legátlagosabb szám? (legkevésbé tér el az átlagtól)
#
import math


def create_lst():
    return [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
            100, 67, 22, 8, -78, -6]


def is_kobszam(n):
    cube = n ** (1 / 3)
    if cube ** 3 == n:
        return True
    else:
        return False


def fel_1(lst):
    for i in range(len(lst) - 1, -1, -1):
        if is_kobszam(lst[i]):
            print(lst[i])
            break


def fel_2(lst):
    return len(lst)


def fel_3(lst):
    osszeg = 0
    for i in range(len(lst) - 1):
        result = lst[i + 1] - lst[i]
        osszeg += result
    return osszeg


def fel_4(lst):
    van = False
    for i in range(1, len(lst) - 1):
        if lst[i - 1] % i == 0:
            van = True
            break
    return 'Van' if van == True else 'Nincs'


def fel_5(lst):
    kulonbseg = lst[1] - lst[0]
    for i in range(1, len(lst) - 1):
        if lst[i + 1] - lst[i] != kulonbseg:
            return 'Nem igaz'
    return 'Igaz'


# 6. Írjuk ki a sorozatban található első négyzetszám négyzetét!
def is_negyzet_szam(n):
    if n < 0:
        return False
    negyzet = math.isqrt(n)
    if negyzet ** 2 == n:
        return True
    else:
        return False


def fel_6(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            if is_negyzet_szam(n=lst[i]):
                return lst[i] ** 2


def fel_7(lst):
    van = False
    for i in range(len(lst)):
        db_oszto = 0
        for j in range(1, lst[i] + 1):
            if lst[i] % j == 0:
                db_oszto += 1
        if db_oszto == 2:
            van = True
    return 'Van' if van == True else 'Nincs'


def fel_8(lst):
    van = False
    for i in lst:
        if i < -50 or i > 50:
            van = True
    return 'Nem' if van == True else 'Igen'


def fel_9(lst):
    prim_lst = []
    for i in range(len(lst)):
        db_oszto = 0
        for j in range(1, lst[i] + 1):
            if lst[i] % j == 0:
                db_oszto += 1
        if db_oszto == 2:
            prim_lst.append(lst[i])
    return prim_lst


def osszeg(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return osszeg


def fel_10(lst):
    atlag = osszeg(lst) / len(lst)
    l = lst[0]
    lg = abs(lst[0] - atlag)

    for i in lst:
        elteres = abs(i - atlag)
        if elteres < lg:
            lg = elteres
            l = i

    return l

def main():
    lst = create_lst()
    print('1.feladat:')
    fel_1(lst)
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
    print(fel_7(lst))
    print('8.feladat:')
    print(fel_8(lst))
    print('9.feladat:')
    fel_9_lst = fel_9(lst)
    for i in fel_9_lst:
        print(i, end=' ')
    print()

    print('10.feladat:')
    print(fel_10(lst))


if __name__ == '__main__':
    main()
