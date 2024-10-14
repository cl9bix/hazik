# 3. Írd ki a [0;100] intervallumból azokat az egész számokat, melyek 5-ös számjegyre végződnek!
# 4. Olvass be egy egész számot, és írd ki azokat a számokat, melyek ezt a számot osztják!
# 5. Olvass be két egész számot, írd ki a közöttük lévő egész számokat!
# 6. Kérj be 5 számot, és írd ki az összegüket!
# 7. Kérj be egy számot, vizsgáld meg, hogy prímszám-e!

def main(x, y):
    x = 0
    print('Az egesz szamok:')
    while x <= y:
        print(x, end=',')
        x += 1
    print()
    print('5-tel oszthato szamok:')
    x = 0
    while x <= y:
        if x % 5 == 0 and x != 0:
            print(x, end=', ')
        x += 1
    print()
    print('5-os szamjegyre vegeznek:')
    x = 0
    while x <= y:
        if x % 5 == 0 and x % 10 != 0:
            print(x, end=', ')
        x += 1
    print()
    user_num = int(input("Kerek egy egesz szamot: "))
    x = 1
    while x <= user_num:
        try:
            if user_num % x == 0:
                print(x, end=', ')
        except Exception as e:
            pass
        x += 1
    print()
    first_num = int(input("Kerem az 1 szamot: "))
    second_num = int(input("Kerem az 2 szamot: "))
    if first_num < second_num:
        while first_num < second_num - 1:
            print(first_num + 1,end=', ')
            first_num += 1
    else:
        while second_num < first_num - 1:
            print(second_num + 1,end=', ')
            second_num += 1


    print()
    n = 1
    osszeg = 0
    while n < 6:
        user_szam = int(input(f"Kerem az {n}. szamot: "))
        osszeg += user_szam
        n += 1
    print('5 szamnak az osszege:',osszeg)

    db_oszto = 0
    is_prim = int(input('Kerek egy szamot: '))
    n = 1
    while n <= is_prim:
        if is_prim % n == 0:
            db_oszto += 1
        n += 1

    if db_oszto == 2:
        print("Primszam")
    else:
        print("Nem primszam")





if __name__ == '__main__':
    main(x=0, y=100)
