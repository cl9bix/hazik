import random


def main():
    lst = [random.randint(0, 100) for _ in range(10)]
    #     1 feladat
    # lst = [1,1,1,4,3]
    print("Lista elemei:")
    for i in lst:
        print(i, end=' ')
    print()
    print()
    print("1.feladat:")
    for i in range(5):
        print('', lst[i], end=' ')
    print()
    print('2.feladat:')
    for i in lst[-5:]:
        print('', i, end=' ')
    print()
    print('3.feladat')
    print('Az osszeg:', lst[0] + lst[-1])
    masolat = [1, 63, 36, 12, 6, 2, 8, 16, 22, 99]
    masolat.sort()
    print('4.feladat:')
    for i in masolat:
        print('', i, end=' ')
    print()
    print('5.feladat:')
    db = 0
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            db += 1
    print(f' {db}db')
    print('6.feladat:')
    van = False
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            van = True
    if van:
        print(" Van")
    else:
        print("Nincs")

    print('7.feladat:')
    van = False
    for i in range(1, len(lst) - 1):
        if lst[i - 1] == lst[i] == lst[i + 1]:
            van = True
            break
    if van:
        print(" Van")
    else:
        print(" Nincs")
    print('8.feladat:')
    lst_8 = [5, 10, 1, 2, 3, 4, 5, 1, 2, 4, 3, 6, 123, 246]
    van = False
    for i in range(len(lst_8) - 1):
        if lst_8[i] * 2 == lst_8[i + 1]:
            van = True
    if van:
        print(" Van")
    else:
        print(' Nincs')

    print('9.feladat:')
    lst_9 = [random.randint(1, 10) for _ in range(10)]
    sorrend = False
    for i in range(len(lst_9) - 1):
        for j in lst_9:
            if lst_9[i] > j:
                temp = j
                j = lst_9[i]
                lst_9[i] = temp
                sorrend = True
    if sorrend:
        print('Igen')
    else:
        print("Nem")

    print()
    print('10.feladat:')

    lst_10 = [random.randint(0,20) for _ in range(10)]
    # lst_10 =[1,1,6,3,1,4,3]
    print(lst_10)
    for i in range(1,len(lst_10)-1):
        if lst_10[i-1] + lst_10[i+1] == lst_10[i]:
            print('',lst_10[i],end=' ')


if __name__ == '__main__':
    main()
