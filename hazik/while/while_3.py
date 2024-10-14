def main():
    user_num1 = int(input("1Kerek egy szamot(100-500 kozott): "))
    if user_num1 < 100 or user_num1 > 500:
        print('Rossz szam')
    else:
        x = 100
        y = 500

        while x < user_num1:
            if x % 3 == 0 and x % 4 == 0:
                print(x, end=', ')
            x += 1
    print()
    user_num2 = int(input("2Kerek egy szamot(1000-10000 kozott): "))
    print('Az elso szamjegye',user_num2 % 10)
    print()
    q = int(input("3Kerek egy szamot(1000-10000 kozott): "))
    if q >= 1000 and q <= 9999:
        _ = q
        legnagyobb = 0

        while q > 0:
            current = q % 10
            if current > legnagyobb:
                legnagyobb = current
            q //= 10
        print('A legnagyobb:', legnagyobb)

        legkisebb = 9
        q = _
        while q > 0:
            current = q % 10
            if current < legkisebb:
                legkisebb = current
            q = q // 10
        print('A legkisebb:', legkisebb)
        print()

    l = int(input("4Kérek egy számot (1000 - 9999): "))
    f = l // 1000
    s = (l // 100) % 10
    t = (l // 10) % 10
    fr = (l % 10)

    if f == s and t == fr:
        print('Egyforma szamjegyekbol all')
    else:
        print("Nem egyforma szamjegyekbol all")


    # if 1000 <= l <= 9999:
    #     van_egyezes = 0
    #     while l > 0:
    #         current = l % 10
    #         l = l // 10
    #         temp = l
    #         while temp > 0:
    #             if current == temp % 10:
    #                 van_egyezes = 1
    #                 break
    #             temp = temp // 10
    #         if van_egyezes == 1:
    #             break
    #     if van_egyezes == 1:
    #         print("Min ket egyforma szamjegy van benne")
    #     else:
    #         print("Nincsenek egyforma szamjegyek")


if __name__ == '__main__':
    main()
