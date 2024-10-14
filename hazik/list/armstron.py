import random

def main():
    lst = [random.randint(100,999) for _ in range(200)]
    # lst = [153]
    van = True
    print("Armstrong szamok: ")
    db = 0
    for i in lst:

        if (i // 100) ** 3 + ((i // 10) % 10) ** 3 + (i % 10) ** 3 == i:
            print('', i, end=' ')
            db += 1
    if db < 1:
        print('A számok között nincs Armstrong szám!')





if __name__ == '__main__':
    main()
