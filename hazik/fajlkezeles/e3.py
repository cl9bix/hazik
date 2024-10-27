def create_lst():
    lst = []
    with open('03_000.txt', 'r', encoding='utf-8') as f:
        for i in f:
            lst.append(int(i))
    return lst


def kiir(lst):
    for i in lst:
        print(i, end=' ')


def fel_1(lst):
    van = False
    for i in lst:
        if i % 100 == 0:
            van = True
            break
    return "Van" if van == True else 'Nincs'


def fel_2(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 7 == 0:
            return i + 1
            break


def fel_3(lst):
    for i in range(len(lst) - 1):
        if lst[i] % 19 == 0:
            return i + 1
            break


def fel_4(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    atlag = osszeg / len(lst)

    return atlag ** 2


def fel_5(lst):
    kisebb_10 = False
    for i in lst:
        if i < 10:
            kisebb_10 = True
            break
    return 'Igaz' if kisebb_10 == False else 'Nem igaz'


def fel_6(lst):
    db = 0
    for i in lst:
        if i % 9 == 0:
            db += 1
    return db


def fel_7(lst):
    new_lst = []
    for i in lst:
        if i % 15 == 0:
            new_lst.append(i / 2)
    return new_lst

def fel_8(lst):
    return len(lst)

def fel_9(lst):
    van=False
    for i in range(len(lst)-1):
        if lst[i]<0:
            if lst[i+1] > 0:
                van=True
                break
    return 'Van' if van == True else 'Nincs'


def fel_10(lst):
    legkisebb = lst[0]
    for i in range(len(lst)-1):
        if lst[i] < legkisebb:
            legkisebb = lst[i]
    return legkisebb


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
    kiir(fel_7(lst))
    print('8.feladat:')
    print(fel_8(lst))
    print('9.feladat:')
    print(fel_9(lst))
    print('10.feladat:')
    print(fel_10(lst))



if __name__ == '__main__':
    main()
