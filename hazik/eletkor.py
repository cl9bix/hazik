def main():
    eletkor = float(input('Hany eves vagy?: '))
    # lentrol felfele
    if eletkor < 0:
        print('Nincs ilyen eletkor')
    elif eletkor <= 14:
        print('Gyerek')
    elif eletkor <= 23:
        print('kamasz')
    elif eletkor <= 62:
        print('felnot')
    else:
        print("Idos")
    # fentrol lefele
    if eletkor < 0:
        print('Nincs ilyen eletkor')
    elif eletkor >= 63:
        print('Idos')
    elif eletkor >= 24:
        print('felnot')
    elif eletkor >= 15:
        print('kamasz')
    else:
        print("Gyerek")

# intervallum modszer

    if eletkor < 0:
        print('Nincs ilyen eletkor')
    else:
        if eletkor >= 0 and eletkor <=14:
            print('Gyerek')
        if eletkor >= 15 and eletkor <=23:
            print('kamasz')
        if eletkor >= 24 and eletkor <=62:
            print('felnot')
        if eletkor > 62:
            print('Idos')

if __name__ == '__main__':
    main()
