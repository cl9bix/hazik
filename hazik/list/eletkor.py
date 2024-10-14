import random


def main():
    lst = [random.randint(0, 90) for _ in range(20)]
    kor1 = 0
    kor2 = 0
    kor3 = 0
    kor4 = 0
    for i in range(len(lst)):
        if lst[i] <= 14:
            print('Gyerek')
            kor1 += 1
        elif lst[i] <= 23:
            print('Kamasz')
            kor2 += 1
        elif lst[i] <= 62:
            kor3 += 1
            print('felnott')
        else:
            kor4 += 1
            print("Idos")
    print()
    korok = [kor1, kor2, kor3, kor4]
    korok1 = [kor1, kor2, kor3, kor4]
    masolat = korok
    masolat.sort(reverse=True)
    print(f"Gyerekek: {kor1}")
    print(f"Kamasz: {kor2}")
    print(f"Felnott: {kor3}")
    print(f"Idos: {kor4}")

    print(f'Legtobb - kor{korok1.index(masolat[0]) + 1} van a legtobben')

    print('Van 50 eves' if 50 in lst else 'Nincs')
    osszeg = 0
    for i in lst:
        osszeg += i
    print(f'Atlag - {osszeg / len(lst)}')
    k_osszeg = 0
    for i in lst:
        if i <= 14:
            k_osszeg += i
    print(f'Kamaszok atlageletkora: {k_osszeg / kor1}')
    lst_masolat = lst.copy()
    lst_masolat.sort()
    print(lst_masolat[-1], 'eves a legidosebb ember')
    print(lst_masolat[0], f'eves a legfiatalabb ember es {lst.index(lst_masolat[0])} helyen all.')

    felnottek = [i for i in lst if i > 23 and i < 63]
    felnottek.sort()
    print("Felnottek csokkeno sorrendbe:")
    for i in felnottek:
        print(i, end=' ')
    age = int(input('Kerem az eletkort: '))
    if age in lst:
        print(f"A(z) {age} eletkor szerepel a listaba")
    else:
        print(f'{age} nem szerepel a listaba')

if __name__ == '__main__':
    main()
