def create_lst():
    lst = []
    with open('kor.txt', 'r', encoding='utf-8') as f:
        for i in f:
            lst.append(int(i))
    return lst


def kiir(lst):
    for i in lst:
        print(i, end=' ')


def fel_1(lst):
    for i in lst:
        if i <= 14:
            print("Gyerek")
        elif i <= 23:
            print('Kamasz')
        elif i <= 62:
            print('Felnott')
        elif i >= 63:
            print('Idos')


def fel_2(lst):
    kor1 = 0
    kor2 = 0
    kor3 = 0
    kor4 = 0
    for i in lst:
        if i <= 14:
            kor1 += 1
        elif i <= 23:
            kor2 += 1
        elif i <= 62:
            kor3 += 1
        elif i >= 63:
            kor4 += 1
    return [kor1, kor2, kor3, kor4]


def fel_3(data):
    masolat = data.copy()

    masolat.sort(reverse=True)
    legnagyobb = masolat[0]

    for i in range(len(data)):
        if data[i] == legnagyobb:
            return i + 1


def fel_4(lst):
    return 'Igen' if 50 in lst else 'Nem'


def fel_5(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return osszeg / len(lst)


def fel_6(lst):
    new_lst = list(x for x in lst if x >= 15 and x <= 23)
    osszeg = 0
    for i in new_lst:
        osszeg += i
    return osszeg / len(new_lst)


def fel_7(lst):
    legidosebb = lst[0]
    idx=0
    for i in range(len(lst)):
        if lst[i] > legidosebb:
            legidosebb = lst[i]
            idx=i
    return legidosebb,idx+1

def fel_8(lst):
    legfiatalabb=lst[0]
    idx=0
    for i in range(len(lst)):
        if lst[i] < legfiatalabb:
            legfiatalabb=lst[i]
            idx=i
    return legfiatalabb,idx+1


def fel_9(lst):
    new_lst = list(x for x in lst if x >= 24 and x <= 63)
    masolat = new_lst.copy()
    masolat.sort()
    return masolat



def fel_10(lst,age):
    return f'{age} Szerepel' if age in lst else f'{age} Nem szerepel'




def main():
    lst = create_lst()
    print('1.feladat:')
    print(fel_1(lst))
    print('2.feladat:')
    print(fel_2(lst))
    print('3.feladat:')
    print(f'Kor_{fel_3(fel_2(lst))}')
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
    kiir(fel_9(lst))
    print()
    print('10.feladat:')
    user_age = int(input('Kerek egy eletkor: '))

    print(fel_10(lst,user_age))


if __name__ == '__main__':
    main()
