# 1. Mennyi a sorozatban található számok szorzata?
# 2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
# 3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
# 4. Igaz-e, hogy minden szám negatív?
# 5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
# 6. Hány 18-cal osztható szám található a sorozatban?
# 7. Mennyi a sorozatban található egyik legkisebb szám indexe?
# 8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
# 9. Hány eleme van a sorozatnak?
# 10. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?


def create_lst():
    return [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
            100, 67, 22, 8, -78, -6]


def fel_1(lst):
    szorzat = 1
    for i in lst:
        szorzat *= i
    return szorzat


def fel_2(lst):
    idx = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 5 == 0 or lst[i] % 7 == 0:
            idx = i
            print(lst[i], '-', 'index:', idx + 1)
            break


# 3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
def fel_3(lst):
    idx = 0
    for i in range(len(lst) - 1):
        if lst[i] % 3 == 0 and lst[i] % 7 == 0:
            idx = i
            print(lst[i], '-', 'index:', idx + 1)
            break


# 4. Igaz-e, hogy minden szám negatív?
def fel_4(lst):
    van_poz = False
    for i in lst:
        if i > 0:
            van_poz = True
            break
    return 'Nem' if van_poz == True else 'Igaz'


# Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
def fel_5(lst):
    van = False
    for i in lst:
        if i > 0 and i < 11:
            van = True
            break
    return 'Van' if van == True else 'Nincs'


# 6. Hány 18-cal osztható szám található a sorozatban?
def fel_6(lst):
    db = 0
    for i in lst:
        if i % 18 == 0:
            db += 1
    return db


# 7. Mennyi a sorozatban található egyik legkisebb szám indexe?
def fel_7(lst):
    masolat = lst.copy()
    masolat.sort()
    get_first = masolat[0]
    return lst.index(get_first)


# 8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
def fel_8(lst):
    new_lst = []
    for i in lst:
        if i % 17 == 0 or i % 18 == 0:
            print(i)
            new_lst.append(i ** 2)
    return new_lst


# 10. Van-e a sorozatban olyan negatív szám,
# amelynek az összes szomszédja pozitív?

def fel_9(lst):
    van = False
    for i in range(1, len(lst) - 1):
        if lst[i] < 0:
            if lst[i - 1] > 0 and lst[i + 1] > 0:
                van = True
    return 'Van' if van == True else 'Nincs'


def main():
    lst = create_lst()
    print('1.feladat:')
    print(fel_1(lst))
    print('2.feladat:')
    fel_2(lst)
    print('3.feladat:')
    fel_3(lst)
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
    print(len(lst), 'eleme van')
    print('10.feladat')
    print(fel_9(lst))


if __name__ == '__main__':
    main()
