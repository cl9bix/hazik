class Data:
    def __init__(self, sor):
        data = sor.split(';')
        self.ora = int(data[0])
        self.perc = int(data[1])
        self.adasdb = int(data[2])
        self.nev = data[3].strip()


def create_lst():
    lst = []
    with open(file='cb.txt', mode='r', encoding='utf-8') as f:
        next(f)
        for i in f:
            obj = Data(i)
            lst.append(obj)

    return lst


# def kiir(lst):
#     for i in lst:
#         print(f'{i.ora} {i.perc} {i.adasdb} {i.nev}')




def fel_4(lst):
    van=False
    for i in range(len(lst)-1):
        db = 0
        for j in range(i+1,len(lst)):
            if lst[i].perc == lst[j].perc:
                db+= 1
        if db == 4:
            van=True
            break
    return 'Volt negy adast indito sofor' if van == True else 'Nem volt negy adast indito sofor'


def fel_5(lst,name:str):
    db=0
    for i in lst:
        if i.nev == name:
            db+=i.adasdb
    return f'{name} {db}x hasznalta a CB-radiot' if db>1 else 'Nincs ilyen nevu sofor !'




def AtszamolPercre(ora,perc):
    result = ora * 60
    return result + perc

def fel_7(lst):
    with open(file='cb2.txt',mode='w',encoding='utf-8') as f:
        f.write('Kezdes;Nev;AdasDb\n')
        for i in lst:
            ido = AtszamolPercre(i.ora,i.perc)
            f.write(f'{ido};{i.nev};{i.adasdb}\n')



def fel_8(lst):
    egyedi = []
    for i in lst:
        if i.nev not in egyedi:
            egyedi.append(i.nev)
    return len(egyedi)


def fel_9(lst):
    dct={}
    for i in lst:
        if i.nev not in dct:
            dct[i.nev] = i.adasdb
        else:
            dct[i.nev] += i.adasdb
    return (max(dct,key=dct.get),dct[max(dct,key=dct.get)])



def main():
    lst = create_lst()
    # kiir(lst)
    print(f'3.feladat: Bejegyzesek szama: {len(lst)}')
    print(f'4.feladat: ')
    print(fel_4(lst))
    user_name = input('5.feladat: Kerek egy nevet: ')
    print(fel_5(lst,name=user_name))
    fel_7(lst)
    print(f'8.feladat: Soforok szama: {fel_8(lst)} fo')
    print(f'''9.feladat: Legtobb adast indito sofor:
      Nev: {fel_9(lst)[0]}
      Adasok szama: {fel_9(lst)[1]}''')



if __name__ == '__main__':
    main()





