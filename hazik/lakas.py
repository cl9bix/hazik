import random


def main():
    kolcsonosszeg = float(input('Kölcsönösszeg: '))
    evi_kamat = float(input('Évi kamat(%): '))
    futamido = float(input('Futamidő(evekben): '))

    vegosszeg = kolcsonosszeg * (1 + (evi_kamat / 100) * futamido)

    print(round(vegosszeg, 2), 'FT', 'adott vissza kell fizetni.')
    print()

    ranom_nums = []
    for i in range(5):
        num = random.randint(200000, 2000000)
        ranom_nums.append(num)

    print('Generalt szamok: ')
    for q in ranom_nums:
        print(' ', q, 'FT')
    print()

    if vegosszeg > 0 and vegosszeg < 300000:
        print(f"{vegosszeg}FT - Alacsony")
    elif vegosszeg > 300001 and vegosszeg < 500000:
        print(f"{vegosszeg}FT - Kozepes")

    elif vegosszeg > 500001 and vegosszeg < 1000000:
        print(f"{vegosszeg}FT - Magas")

    elif vegosszeg > 1000001:
        print(f"{vegosszeg}FT - Nagyon Magas")


if __name__ == '__main__':
    main()
