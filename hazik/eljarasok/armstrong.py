import random


def create_lst():
    return [random.randint(100, 999) for _ in range(200)]


def armstrong_num(lst):
    for i in lst:
        first = i // 100
        second = (i // 10) % 10
        third = i % 10
        if (first ** 3) + (second ** 3) + (third ** 3) == i:
            print(i, end=' ')


def main():
    lst = create_lst()
    armstrong_num(lst)


if __name__ == '__main__':
    main()
