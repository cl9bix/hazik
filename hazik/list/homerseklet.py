# 1. Ajak települesen 2 hèten keresztül megmèrjük a hőmérsékletet minden nap 11:00 kor. Az tudjuk hogy a hőmérséklet 32 -39 fok közè esik. Generáld le egy listába az adott hömèrsèkleteket!
# 2. Írd ki a hőmérsékleteket a képernyőre.
# 3. Hányszor szerepelnek az egyes hőmérsékletek?
# 4. Van e olyan hőmérséklet amit nem mèrtek 32-39 es intervallumban?

import random

def main():

    lst = [random.randint(32,39) for _ in range(14)]
    print('Homersekletek:')
    for i in lst:
        print('',i,end=' ')
    print('')
    for i in range(len(lst)):
        db = 0
        for j in lst:
            if lst[i]==j:
                db+=1
        print(f'Az {lst[i]} - {db}szor szerepel.')

    print()
    van = True
    for i in lst:
        if i < 32 and i > 39:
            van = True
        else:
            van = False
    if van == True:
        print("van")
    else:
        print("nincs")

if __name__ == '__main__':
    main()