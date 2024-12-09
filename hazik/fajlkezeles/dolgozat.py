def create_lst():
    lst = []
    with open('osztalyzat.txt', 'r', encoding='utf-8') as f:
        for i in f: lst.append(int(i))

    return lst


def kiir(lst):
    for i in lst:
        print(i, end=' ')


def fel_1(lst):
    for i in lst:
        if i <= 60:
            print('Elegtelen')
        elif i <= 70:
            print('Elegseges')
        elif i <= 80:
            print('Kozepes')
        elif i <= 90:
            print('Jo')
        else:
            print('Jeles')


def fel_2(lst):
    jeles = 0
    jo = 0
    kozepes = 0
    elegseges = 0
    elegtelen = 0
    for i in lst:
        if i <= 60:
            elegtelen += 1
        elif i <= 70:
            elegseges += 1
        elif i <= 80:
            kozepes += 1
        elif i <= 90:
            jo += 1
        else:
            jeles += 1

    return [jeles, jo, kozepes, elegseges, elegtelen]


def fel_3(lst):
    osszeg = 0
    for i in lst:
        osszeg += i
    return osszeg / len(lst)


def fel_4(lst):
    legkevesebb = lst[0]
    idx = 0
    for i in range(len(lst)):
        if lst[i] < legkevesebb:
            legkevesebb = lst[i]
            idx = i + 1
    return legkevesebb, idx


def fel_5(lst):
    legmagasabb = lst[0]
    for i in range(len(lst)):
        if lst[i] > legmagasabb:
            legmagasabb = lst[i]
    return legmagasabb


def fel_6(lst):
    new_lst = [x for x in lst if x >= 61 and x <= 70]
    legkisebb = new_lst[0]
    for i in range(len(new_lst)):
        if new_lst[i] < legkisebb:
            legkisebb = new_lst[i]
    return legkisebb

def fel_7(lst,num):
    return f'Van {num}' if num in lst else f'Nincs {num}'


def main():
    lst = create_lst()
    print('1.feladat:')
    fel_1(lst)
    print('2.feladat:')
    data = fel_2(lst)
    print('Jeles:',data[0])
    print('jo:',data[1])
    print('Kozepes:',data[2])
    print('Elegseges:',data[3])
    print('Elegtelen:',data[4])



    print('3.feladat:')
    print(round(fel_3(lst), 2))
    print('4.feladat:')
    print(fel_4(lst))
    print('5.feladat:')
    print(fel_5(lst))
    print('6.feladat:')
    print(fel_6(lst))
    print('7.feladat:')
    print(fel_7(lst,num=50))


if __name__ == '__main__':
    main()
