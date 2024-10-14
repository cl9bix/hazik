def main():
    value = input('Kérem adja meg miből kiván átváltani: (F/D): ')
    if value == 'F' or value == 'f':
        money = 'forintot'
    elif value =='D' or value =='d':
        money = 'dollart'
    else:
        print('Hiba')
        return
    amount = int(input(f'Kérem adja meg az átváltani kivánt {money}: '))
    course = 365
    if value == 'F' or value =='f':
        forint_amount = amount / course
        print(f'Ezért az összegért {forint_amount} dollárt fog kapni.')
    elif value =='D' or value =='d':
        dollar_amount = amount * course
        print(f'Ezért az összegért {dollar_amount} forintot fog kapni.')



if __name__ == '__main__':
    main()