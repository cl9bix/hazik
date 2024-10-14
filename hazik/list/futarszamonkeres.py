import random


def main():
    lst = [random.randint(1, 20) for _ in range(10)]
    print('1. feladat:')
    ut1 = 0
    ut2 = 0
    ut3 = 0
    ut4 = 0
    ut5 = 0
    utak = []
    for i in lst:
        if i <= 3:
            print(f'{i}km utra 500ft kapott.')
            ut1 += 1
        elif i <= 7:
            ut2 += 1
            print(f'{i}km utra 700ft kapott.')
        elif i <= 11:
            ut3 += 1
            print(f'{i}km utra 900ft kapott.')

        elif i <= 15:
            ut4 += 1
            print(f'{i}km utra 1400ft kapott.')

        elif i <= 20:
            ut5 += 1
            print(f'{i}km utra 2000ft kapott.')
    print()
    print('2.feladat:')
    osszesen = 0
    for i in range(len(lst)):
        osszesen += lst[i]
    print(' Osszesen:', osszesen)
    print()
    print('3.feladat:')
    print(f' atlagosan:{osszesen/len(lst)}' if osszesen / len(lst) > 0 else 'Nincs')
    print()
    utak = [ut1,ut2,ut3,ut4,ut5]
    print('4.feladat:')
    for i in range(len(utak)):
        print(f'Az ut_{i + 1}. kategoriara - {utak[i]} ut eset')
    print()

    print('5.feladat:')
    masolat = [ut1, ut2, ut3, ut4, ut5]
    utak = [ut1, ut2, ut3, ut4, ut5]
    utak.sort(reverse=True)
    print(f'ut_{masolat.index(utak[0]) + 1}')
    print()
    print('6.feladat:')
    print('Szerepel 15' if 15 in lst else 'Nem szerepel 15')
    print()
    # 7.feladat
    lst_7 = [i for i in lst if i > 6 and i < 10]
    osszeg = 0
    for i in lst_7:
        osszeg += i
    print()
    print(f'8.feladat:\n Atlagosan: {osszeg / len(lst_7)} km utak hossza')
    print()
    masolat = [ut1, ut2, ut3, ut4, ut5]
    utak = [ut1, ut2, ut3, ut4, ut5]
    utak.sort(reverse=True)
    print(f'9.feladat:\nLeghosszabb Ut_{masolat.index(utak[0]) + 1}')
    print()
    print('10.feladat:')
    masolat2 = [ut1, ut2, ut3, ut4, ut5]
    utak2 = [ut1, ut2, ut3, ut4, ut5]
    utak2.sort()
    print(f'Legrovidebb Ut_{masolat.index(utak[0]) + 1}')
    print('11.feladat:')
    print()
    van = False
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            van=True
    print('Van' if van == True else 'Nincs')


if __name__ == '__main__':
    main()
