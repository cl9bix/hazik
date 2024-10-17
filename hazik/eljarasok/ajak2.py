# 1. Ajak települesen 2 hèten keresztül megmèrjük a hőmérsékletet minden nap 11:00 kor. Az tudjuk hogy a hőmérséklet 32 -39 fok közè esik. Olvasd be az ajak.txt állományból hömèrsèkleteket!
# 2. Írd ki a hőmérsékleteket a képernyőre.
# 3. Hányszor szerepelnek az egyes hőmérsékletek?
# 4. Hányszor szerepel 35 től nagyobb hőmérséklet?
# 7. Mennyi az átlaghőmérséklet?


import random


def create_lst():
    return [random.randint(32, 39) for _ in range(14)]


def kiir(lst):
    for i in lst:
        print(i, end=' ')


def fel_2(lst):
    completed = []
    for i in range(len(lst)):
        if lst[i] not in completed:
            db = 0
            for j in range(len(lst)):
                if lst[i] == lst[j]:
                    db += 1
            completed.append(lst[i])
            print(f'{lst[i]} - {db}db')


def fel_3(lst):
    homersekletek = [i for i in range(32, 40)]
    print(homersekletek)
    van = False
    for i in range(len(homersekletek)):
        if homersekletek[i] not in lst:
            van = True
            break
    return 'Van' if van == True else 'Nincs'


def fel_4(lst):
    db = 0
    for i in lst:
        if i > 35:
            db += 1
    return db

def fel_5(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return osszeg

def main():
    lst = create_lst()
    print('1.feladat:')
    kiir(lst)
    print()
    print()
    print('2.feladat:')
    fel_2(lst)
    print()
    print('3.feladat:')
    print(fel_3(lst))
    print('4.feladat:')
    print(fel_4(lst))
    print('5.feladat:')
    osszeg = fel_5(lst)
    print(osszeg / len(lst))

if __name__ == '__main__':
    main()
