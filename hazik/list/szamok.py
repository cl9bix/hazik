import random


def main():
    lst = [random.randint(-120, 20) for _ in range(15)]
    poz = 0
    poz_db = 0
    neg = 0
    for i in lst:
        if i > 0:
            poz += i
            poz_db += 1
        elif i % 2 != 0 and i < 0:
            neg += 1
    print("Pozitiv szamok osszege:", poz)
    print("negatív páratlan számok darabszáma :", neg)

    print("Pozitiv szamok atlaga:", poz / poz_db)

    lst_5 = lst.copy()
    lst_5.sort()
    print('Legnagyobb szam:', lst_5[-1])
    print('Legkisebb szam:', lst.index(lst_5[0]))

    lst_5.sort(reverse=True)
    print("Csokkeno sorrend:")
    for i in lst_5:
        print(i, end=' ')
    print()
    van = False
    for i in range(len(lst) - 1):
        if lst[i] and lst[i + 1] < 0:
            van = True
            break
    print("Van" if van == True else "Nincs")

    van6 = False
    for i in range(len(lst) - 1):
        if lst[i] + lst[i + 1] == 6:
            van6 = True
            break
    print("Van 6" if van6 == True else "Nincs")

    db = 0
    van10 = False
    for i in range(1, len(lst) - 1):
        if lst[i - 1] and lst[i + 1] > lst[i]:
            van10 = True
            db += 1
    print(f'Van, {db}db' if van10 == True else 'Nincs')

    van11 = False
    for i in range(1, len(lst) - 1):
        if lst[i - 1] and lst[i + 1] == 0:
            van11 = True
            idx = lst.index(i)
    print(f'Van, {idx}. ez a szam' if van11 == True else 'Nincs')

    lst_12 = []
    for i in lst:
        if i % 2 != 0:
            lst_12.append(i)
    print('Novekvo sorrend')
    lst_12.sort()
    for i in lst_12:
        print(i, end=' ')
    print()
    lst_13 = []
    for i in lst:
        if i % 3 == 0:
            lst_13.append(i)
    print('3-mal oszthato csokkeno sorrendbe:')
    for i in lst_13:
        print(i, end=' ')
    

if __name__ == '__main__':
    main()
