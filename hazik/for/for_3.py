def main():
    elso_szam = int(input("1.Kerek egy szamot [100;500]: "))
    for i in range(1, elso_szam + 1):
        if i % 3 == 0 and i % 4 == 0:
            print(i, end=',')
    print()
    number = int(input('Kerek egy szamot [1000;10000]: '))
    print()
    print(f' elso szamjegye: {number % 10}')
    f = number // 1000
    s = (number // 100) % 10
    t = (number // 10) % 10
    fr = number % 10
    if f > s and f > t and f > fr:
        legnagyobb = f
    elif s > f and s > t and s > fr:
        legnagyobb = s
    elif t > f and t > s and t > fr:
        legnagyobb = t
    elif fr > f and fr > t and fr > s:
        legnagyobb = fr
    else:
        legnagyobb =f
    print(f' legnagyobb szamjegye: {legnagyobb}')

    if f <= s and f <= t and f <= fr:
        legkisebb = f
    elif s <= f and s <= t and s <= fr:
        legkisebb = s
    elif t <= f and t <= s and t <= fr:
        legkisebb = t
    else:
        legkisebb = fr
    print(f' legkisebb szamjegye: {legkisebb}')

    if f == s and f == t and f == fr:
        print(" Egyforma szamjegyekbol all")
    else:
        print(" Nem egyforma szamjegyekbol all")



if __name__ == '__main__':
    main()
