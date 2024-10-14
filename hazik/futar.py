def main():
    tavolasag = float(input('Irjon be egy tetszőleges távolságot: '))
    # lentrol felfele
    if tavolasag < 1 or tavolasag > 30:
        print('Nincs ilyen ut')
    elif tavolasag >= 1 and tavolasag <= 2:
        print('500ft')
    elif tavolasag >= 3 and tavolasag <= 5:
        print('700ft')
    elif tavolasag >= 6 and tavolasag <= 10:
        print('900ft')
    elif tavolasag >= 11 and tavolasag <= 20:
        print('1400ft')
    else:
        print('2000ft')
    # fentrol lefele
    if tavolasag < 1 or tavolasag > 30:
        print('Nincs ilyen ut')
    elif tavolasag >= 21 and tavolasag <= 30:
        print('2000ft')
    elif tavolasag >= 11 and tavolasag <= 20:
        print('1400ft')
    elif tavolasag >= 6 and tavolasag <= 10:
        print('900ft')
    elif tavolasag >= 3 and tavolasag <= 5:
        print('700ft')
    elif tavolasag >= 1 and tavolasag <= 2:
        print('500ft')

# intervallum modszer

    if tavolasag < 1 or tavolasag > 30:
        print('Nincs ilyen ut')
    else:
        if tavolasag >= 1 and tavolasag <=2:
            print('500ft')
        if tavolasag >= 3 and tavolasag <=5:
            print('700ft')
        if tavolasag >= 6 and tavolasag <=10:
            print('900ft')
        if tavolasag >= 11 and tavolasag <=20:
            print('1400ft')
        if tavolasag >= 21 and tavolasag <=30:
            print('2000ft')

if __name__ == '__main__':
    main()
