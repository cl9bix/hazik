import random


def main():
    lst = [random.randint(1, 100) for i in range(25)]
    print(lst)
    for i in range(1, len(lst) + 1):
        print(f'Az {i}. diak - {lst[i - 1]}% osztalyzatot kapot')

    db = 0
    jeles = 0
    jo = 0
    kozepes = 0
    elegseges = 0
    elegtelen = 0
    for j in lst:
        if j >= 0:
            elegtelen += 1
        if j >= 61:
            elegseges += 1
        if j >= 71:
            kozepes += 1
        if j >= 81:
            jo += 1
        if j >= 91:
            jeles += 1
    print()
    print('jeles', jeles)
    print('jo', jo)
    print('kozepes', kozepes)
    print('elegseges', elegseges)
    print('elegtelen', elegtelen)
    print()

    osszeg = 0
    for i in range(len(lst)):
        osszeg += lst[i]
    print(f'A jegyek atlaga: {osszeg / len(lst)}')


if __name__ == '__main__':
    main()
