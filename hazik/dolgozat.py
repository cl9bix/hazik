def main():
    pont = float(input('Irjon be a pontszamot: '))
    # lentrol felfele
    if pont < 0 or pont > 100:
        print('Nincs ilyen pont')
    elif pont >= 0 and pont <= 60:
        print('Elegtelen')
    elif pont >= 61 and pont <= 70:
        print('Elegseges')
    elif pont >= 71 and pont <= 80:
        print('Kozepes')
    elif pont >= 81 and pont <= 90:
        print('Jo')
    elif pont >= 91 and pont <= 100:
        print('Jeles')
    # fentrol lefele
    if pont < 0:
        print('Nincs ilyen pont')
    elif pont <= 60:
        print('Elegtelen')
    elif pont <= 70:
        print('Elegseges')
    elif pont <= 80:
        print('Kozepes')
    elif pont <= 90:
        print('Jo')
    elif pont <= 100:
        print('Jeles')


# intervallum modszer

    if pont < 0:
        print('Nincs ilyen pont')
    else:
        if pont >= 0 and pont <=60:
            print('Elegtelen')
        if pont >= 61 and pont <=70:
            print('Elegseges')
        if pont >= 71 and pont <=80:
            print('Kozepes')
        if pont >= 81 and pont <=90:
            print('Jo')
        if pont >= 91 and pont <= 100:
            print('Jeles')

if __name__ == '__main__':
    main()
