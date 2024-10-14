# A futár az egyes utakra az út hosszától függően kap fizetést az alábbi táblázatnak
# megfelelően:
# 1 – 2 km 500 Ft
# 3 – 5 km 700 Ft
# 6 – 10 km 900 Ft
# 11 – 20 km 1 400 Ft
# 21 – 30 km 2 000
# Generálj 10 db utat 1-30km között,
# majd írd ki mindegyik útra hány ft kapott rá!

# Hány fandintot kapott az összesen a 10 útra?
# Ezt is írja a képernyőre!
import random

def main():
    osszesen = 0
    for i in range(10):
        random_num = random.randint(1, 30)
        print(f'A {random_num}kilometeres utra kap:')
        ut = random_num
        if ut >= 1 and ut <= 2:
            osszesen += 500
            print(' 500ft\n')
        elif ut >= 3 and ut <= 5:
            osszesen += 700
            print(' 700ft\n')
        elif ut >= 6 and ut <= 10:
            osszesen += 900
            print(' 900ft\n')
        elif ut >= 11 and ut <= 20:
            osszesen += 1400
            print(' 1400ft\n')
        elif ut >= 21 and ut <= 30:
            osszesen += 2000
            print(' 2000ft\n')
    print('Osszesen:',osszesen)

if __name__ == '__main__':
    main()
