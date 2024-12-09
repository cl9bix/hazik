class Data:
    def __init__(self,sor):
        self.helyezes = int(sor.split(' ')[0])
        self.sportolo_szam = int(sor.split(' ')[1])
        self.sport_tag = sor.strip().split(' ')[2]
        self.verseny_neve = sor.strip().split(' ')[3]


def create_lst():
    lst = []
    # sub_list=[]
    with open(file='helsinki_emelt/helsinki.txt',mode='r',encoding='utf-8') as f:
        for i in f:
            obj = Data(i)
            lst.append(obj)
    return lst


def kiir(lst):
    for i in lst:
        print(f"{i.helyezes} {i.sportolo_szam} {i.sport_tag} {i.verseny_neve}")


def fel_4(lst):
    bronza=0
    arany=0
    ezust=0

    for i in lst:
        if i.helyezes == 1:
            arany += 1
        elif i.helyezes == 2:
            ezust += 1
        elif i.helyezes == 3:
            bronza += 1
    return arany,ezust,bronza

def fel_5(lst):
    osszesen=0
    for i in lst:
        if i.helyezes == 1:
            osszesen += 7
        elif i.helyezes == 2:
            osszesen += 5
        elif i.helyezes == 3:
            osszesen += 4
        elif i.helyezes == 4:
            osszesen += 3
        elif i.helyezes == 5:
            osszesen += 2
        elif i.helyezes == 6:
            osszesen += 1
        
    return osszesen


def fel_6(lst):
    uszas = 0
    torna = 0
    for i in lst:
        if i.sport_tag == 'uszas':
            uszas+= i.sportolo_szam
        elif i.sport_tag == 'torna':
            torna += i.sportolo_szam
    return "Uszas" if uszas > torna else "Torna"



def fel_7(lst):
    for i in lst:
        tag:str = i.sport_tag
        if tag == 'kajakkenu':
            new_tag = tag.replace('kajakkenu','kajak-kenu')
            with open(file='helsinki_emelt/helsinki2.txt',mode='a',encoding='utf-8') as f:
                f.write(f'{i.helyezes} {i.sportolo_szam} {new_tag} {i.verseny_neve}\n')
        else:
            with open(file='helsinki_emelt/helsinki2.txt',mode='a',encoding='utf-8') as f:
                f.write(f'{i.helyezes} {i.sportolo_szam} {i.sport_tag} {i.verseny_neve}\n')
                


def fel_8(lst):
    legnagyobb = lst[0].sportolo_szam
    idx=0
    for i in range(len(lst)):
        if lst[i].sportolo_szam > legnagyobb:
            legnagyobb = lst[i].sportolo_szam
            idx = i
    return lst[idx].helyezes,lst[idx].sportolo_szam,lst[idx].sport_tag,lst[idx].verseny_neve

    



def main():
    lst = create_lst()
    # kiir(lst)
    print(f"3.feladat:")
    print(f'Pontszerzo helyezesek szama: {len(lst)} ')
    # print(fel_4(lst))
    print('4. feladat:')
    print('Arany',fel_4(lst)[0])
    print('Ezust',fel_4(lst)[1])
    print('Bronza',fel_4(lst)[2])
    print(f'5.feladat:')
    print('Olimpiai ponto szama:',fel_5(lst))
    print('6.feladat:')
    print(fel_6(lst),'sportagban szereztek a legtobb pontot')
    fel_7(lst)
    # print(fel_8(lst))
    data_8 = fel_8(lst)
    print('8.feladat:')
    print(f'Helyezes: {data_8[0]}\nSportag: {data_8[2]}\nVersenyszam: {data_8[3]}\nSportolok szama: {data_8[1]}')

if __name__=="__main__":
    main()