def main():
    weight = float(input('Irja be a sulyat(kg): '))
    lenght = float(input('Irja be a magassagat(cm): '))
    #     intervallum modszer

    if weight < 0 or lenght < 0:
        print('Hiba')
    else:
        lenght = lenght/ 100
        testtomeg_index = weight / lenght ** 2
        print(testtomeg_index)
        if testtomeg_index < 16:
            print('súlyos soványság')
        if testtomeg_index >=16 and testtomeg_index <=16.99:
            print('mérsékelt soványság')
        if testtomeg_index >= 17 and testtomeg_index <= 18.49:
            print('enyhe soványság')
        if testtomeg_index >= 18.5 and testtomeg_index <= 24.99:
            print("normális testsúly")
        if testtomeg_index >= 25 and testtomeg_index <= 29.99:
            print("túlsúlyos")
        if testtomeg_index >= 30 and testtomeg_index <= 34.99:
            print("	I. fokú elhízás")
        if testtomeg_index >= 35 and testtomeg_index <= 39.99:
            print("II. fokú elhízás")
        if testtomeg_index >= 40:
            print("III. fokú (súlyos) elhízás")
# lentrol felfele:

    if weight < 0 or lenght < 0:
        print('Hiba')
        return

    if testtomeg_index < 16:
            print('súlyos soványság')
    elif testtomeg_index >=16 and testtomeg_index <=16.99:
            print('mérsékelt soványság')
    elif testtomeg_index >= 17 and testtomeg_index <= 18.49:
            print('enyhe soványság')
    elif testtomeg_index >= 18.5 and testtomeg_index <= 24.99:
            print("normális testsúly")
    elif testtomeg_index >= 25 and testtomeg_index <= 29.99:
            print("túlsúlyos")
    elif testtomeg_index >= 30 and testtomeg_index <= 34.99:
            print("	I. fokú elhízás")
    elif testtomeg_index >= 35 and testtomeg_index <= 39.99:
            print("II. fokú elhízás")
    elif testtomeg_index >= 40:
            print("III. fokú (súlyos) elhízás")


# lentrol felfele:

    if weight < 0 or lenght < 0:
        print('Hiba')
        return

    if testtomeg_index >=40:
            print("III. fokú (súlyos) elhízás")
    elif testtomeg_index >=35 and testtomeg_index <=39.99:
            print("II. fokú elhízás")
    elif testtomeg_index >= 30 and testtomeg_index <= 34.99:
            print("	I. fokú elhízás")
    elif testtomeg_index >= 25 and testtomeg_index <= 29.99:
            print("túlsúlyos")
    elif testtomeg_index >= 18.5 and testtomeg_index <= 24.99:
            print("normális testsúly")
    elif testtomeg_index >= 17 and testtomeg_index <= 18.49:
            print('enyhe soványság')
    elif testtomeg_index >= 16 and testtomeg_index <= 16.99:
            print('mérsékelt soványság')
    elif testtomeg_index >= 35 and testtomeg_index <= 39.99:
            print('súlyos soványság')






if __name__ == '__main__':
    main()
