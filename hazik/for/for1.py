def main():
    print('[0;100] egesz szamok:')
    for i in range(0,101):
        print(i,end=' ')
    print()
    print()
    print('[0;100] 5tel oszthatoak:')
    for i in range(0,101):
        if i % 5 == 0 and i != 0:
            print(i,end=' ')
    print()
    print()
    print('5-os szamjegyre vegeznek:')
    for i in range(0,100,5):
        if i % 10 != 0:
            print(i,end=' ')
    print()
    print()

    number = int(input('Kerek egy egesz szamot: '))
    print(f'{number}-t a kovetkezo szamok osztoi: ')
    for i in range(1,number+1):
        if number % i == 0:
            print(' ',i,end=' ')

    print()

    for i in range(1,3):
        user_num = int(input(f'Kerem az {i}. szamot: '))
    for k in range(i,user_num):
        print(k,end=' ')
    print()

    osszeg = 0
    for i in range(1,6):
        num = int(input(f'Kerem az {i}. szamot: '))
        osszeg += num
    print(osszeg)
    db_oszto = 0
    is_prim_num = int(input('Kerek egy szamot: '))
    for i in range(1,is_prim_num+1):
        if is_prim_num % i == 0:
            db_oszto+=1
    if db_oszto == 2:
        print("Prim szam")
    else:
        print('Nem prim szam')



if __name__ == '__main__':
    main()