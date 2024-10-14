def main():
    print('1.feladat')
    number = int(input('Kerek egy egesz szamot: '))
    for i in range(1, number + 1):
        if number % i == 0 and i != 1 and i != number:
            print(f'A legkisebb osztoja: {i}')
            break
    print('2.feladat')

    for i in range(number, 1, -1):
        if number % i ==0  and i != 1 and i != number:
            print(f'A legnagyobb osztoja {i}')
            break
    print('3.feladat')
    print(' A páros osztói:')
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0 and number != i:
                print(i, end=' ')
    print()
    print('4.feladat')

    szam = int(input(" Kerek egy szamot(10-150): "))

    if szam < 10 or szam > 150:
        print(' Rossz szam')
    else:
        osszeg = 0
        for i in range(1, szam + 1):
            if szam % i == 0 and szam != i:
                osszeg += i
        if osszeg > szam:
            print(f" A {szam} szam - Bovelkedo")
        else:
            print(f" A {szam} szam - Hiányos")

    print()
    print('6.feladat')

    db_paratlan = 0
    for i in range(1,11):
        new_num = int(input(f'Kerem az {i}. szamot: '))
        if new_num % 2 != 0:
            db_paratlan += 1
        else:
            pass
    print(f'\n{db_paratlan}db paratlan szam van')

    print("7.feladat:")
    num7 = int(input('Kerek egy szamot[4;200]: '))


    for k in range(4,201):
        if num7 % k == 0:
            print(k,end=' ')





if __name__ == '__main__':
    main()
