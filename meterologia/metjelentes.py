class Data:
    def __init__(self,sor):
        self.telepules = sor.strip().split(' ')[0]
        ido = sor.split(' ')[1]
        new_ido = f'{ido[0]}{ido[1]}:{ido[2]}{ido[3]}'
        self.ido = new_ido
        self.szelirany = sor.strip().split(' ')[2]
        self.temp = int(sor.split(' ')[3])


def create_lst():
    lst = []
    with open(file='meterologia/tavirathu13.txt',mode='r',encoding='utf-8') as f:
        for i in f:
            obj = Data(i)
            lst.append(obj)
    return lst

def fel(n:int):
    print(f'{n}.feladat')

def kiir(lst):
    for i in lst:
        print(f'{i.telepules} {i.ido} {i.szelirany} {i.temp}')



def fel_2(lst,telepules_id):
    for i in lst[::-1]:
        if i.telepules == telepules_id:
            return i.ido
            break


def fel_3(lst): 
    minim = lst[0]
    for i in lst:
        if i.temp < minim.temp:
            minim=i

    maxim = lst[0]
    for i in lst: 
        if i.temp > maxim.temp:
            maxim= i
    return minim,maxim


def fel_4(lst) -> list[object]:
    new_lst:list[object] =[]
    for i in lst:
        if i.szelirany == '00000':
            new_lst.append(i)
    return new_lst




def fel_5(lst):
    egyeni = []
    ido_opt = ['01','07','13','19']
    for i in lst:
        if i.telepules not in egyeni:
            egyeni.append(i.telepules)
    dct_kozep ={}
    for i in egyeni:
        db=0
        osszeg=0
        for j in lst:
            time = j.ido
            new_time = time.split(':')[0]
            if i == j.telepules and new_time in ido_opt:
                db += 1
                osszeg += j.temp
        atlag = osszeg/db
        dct_kozep[i] = round(atlag)

    dct_ing ={}
    for i in egyeni:
        maxi = 0
        mini = 100
        for j in lst:
            if i == j.telepules:
                if j.temp > maxi:
                    maxi = j.temp
                if j.temp < mini:
                    mini = j.temp
        dct_ing[i] = maxi - mini    
    return dct_kozep,dct_ing


def get_hastags(string:str):
    res =''
    get_num = string[-1]
    for i in range(int(get_num)):
        res+='#'
    return res

# def get_all_times(lst,telepules):
#     dct = {}
#     egyeni = []
#     for i in lst:
#         if i.telepules not in egyeni:
#             egyeni.append(i.telepules)
    
#     for i in egyeni:
#         time=[]
#         for j in lst:
#             if i == telepules and i==j.telepules:
#                 time.append(j.ido)
#         dct[i] = time
#         time.clear()
#     print(dct)
def get_all_times(lst,telepules):
    response=f'''
{telepules}
'''
    times = []

    for i in lst:
        if i.telepules == telepules:
            times.append(i.ido)

    for i in times:
        for j in lst:
            if j.telepules == telepules:
                pass
    







def fel_6(lst):
    egyeni = []
    for i in lst:
        if i.telepules not in egyeni:
            egyeni.append(i.telepules)
    
    response = []
    for i in egyeni:
        for j in lst:
            if i == j.telepules:
                pass
                # times = get_all_times(lst,telepules='BC')
                # print(times)
                # response.append([i,times,get_hastags(j.szelirany)])
    # print(response)





def main():
    lst=create_lst()
    # kiir(lst)
    fel(2)
    user_telepules_id = input('Adja meg egy település kódját! Település: ')
    print(f'Az utolsó mérési adat a megadott településről {fel_2(lst,user_telepules_id)}-kor érkezett.')
    fel(3)
    fel_3(lst)
    print(f'A legalacsonyabb hőmérséklet: {fel_3(lst)[0].telepules} {fel_3(lst)[0].ido} {fel_3(lst)[0].temp} fok')
    print(f'A legmagasabb hőmérséklet: {fel_3(lst)[1].telepules} {fel_3(lst)[1].ido} {fel_3(lst)[1].temp} fok')
    fel(4)
    if len(fel_4(lst)) == 0:
        print('Nem volt szélcsend a mérések idején.')
    else:
        for i in fel_4(lst):
            print(f'{i.telepules} {i.ido}')
        
    fel(5)
    kozep,ing = map(dict,fel_5(lst))
    for k,v in kozep.items():
        print(f'{k} Középhőmérséklet: {v}; Hőmérséklet-ingadozás: {ing.get(k)}')
    fel(6)
    # fel_6(lst)

if __name__ == "__main__":
    main()