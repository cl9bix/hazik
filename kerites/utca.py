import random


class Data:
    def __init__(self, sor):
        self.telek = int(sor.strip().split(' ')[0])
        self.szelesseg = int(sor.split(' ')[1])
        self.szin = sor.strip().split(' ')[2]


def create_lst():
    lst = []
    with open(file='kerites.txt', mode='r', encoding='utf-8') as f:
        for i in f:
            obj = Data(i)
            lst.append(obj)
    return lst


# def kiir(lst):
#     for i in lst:
#         print(f'{i.telek} {i.szelesseg} {i.szin}')

def fel_3(lst):
    dct = {}
    res = ''
    for i in lst[::-1]:
        if i.telek % 2 == 0:
            res = 'paros'
            break
        else:
            res = 'paratlan'
            break

    hazszam_paros = 0
    hazszam_paratlan = 0
    for i in lst:
        if i.telek == 0:
            hazszam_paros += 2
        else:
            hazszam_paratlan += 1

    return hazszam_paros, res if res == 'paros' else hazszam_paratlan, res


def fel_4(lst):
    van = False
    db = 0
    for i in range(len(lst)-1):
        if lst[i].telek == 1:
            db += 1
            if lst[i].szin == lst[i + 1].szin:
                van = True
                break
    return db if van == True else None


import random

def fel_5(lst, user_hazszam):
    abc = ['A', 'B', 'C', 'D', "E", "F", "G", "H", "I", "W", "Z", 'Y']
    db = 0
    szomszed_1 = ''
    current_szin = ''
    szomszed_2 = ''

    for i in range(len(lst)):
        if lst[i].telek == 1:
            db += 1
        if db == user_hazszam:
            print(lst[i].szin)
            break
            # if i > 0:
            #     szomszed_1 = lst[i - 1].szin
            # current_szin = lst[i].szin
            # if i < len(lst) - 1:
            #     szomszed_2 = lst[i + 1].szin
            # break

    while True:
        random_choice = random.choice(abc)
        if random_choice != szomszed_1 and random_choice != szomszed_2 and random_choice != current_szin:
            return random_choice, current_szin


def main():
    lst = create_lst()
    # kiir(lst)
    print(f'2.feladat\nAz eladott telkek száma: {len(lst)}')
    print(f'3.feladat\nA {fel_3(lst)[1]} oldalon adták el az utolsó telket.')
    print(f'Az utolsó telek házszáma: {fel_3(lst)[0]}')
    print(f'A szomszédossal egyezik a kerítés színe: {fel_4(lst)}')
    user_hazszam = int(input('Adjon meg egy házszámot! '))
    print(fel_5(lst,user_hazszam))
    # print(f'A kerites szine / allapota: {fel_5(lst, user_hazszam)[1]}')
    # print(f'Egy lehetseges festeni szin: {fel_5(lst,user_hazszam)[0]}')


if __name__ == '__main__':
    main()
