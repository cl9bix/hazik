import random


def main():
    dobasok = []
    for i in range(5000):
        dobas = random.randint(1, 6)
        dobasok.append(dobas)

#     1.feladat
    for i in dobasok:
        print(i,end=',')
    for i in range(1,7):
        db = 0
        for j in dobasok:
            if i == j:
                db+=1
        print(f'{i} - {db}db')





    # for i in range(len(dobasok) -1):
    #     db = 0
    #     for j in dobasok:
    #         if dobasok[i] == j:
    #             db += 1
    #
    # for _ in range(1,6):
    #     print(f'A {dobasok[i]} - {db}db van')




if __name__ == '__main__':
    main()
