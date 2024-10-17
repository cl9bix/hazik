import random


def create_lst():
    return [random.randint(1, 6) for _ in range(5000)]


def func(lst):
    completed = []
    for i in range(len(lst)):
        if lst[i] not in completed:
            db = 0
            for j in range(len(lst)):
                if lst[i] == lst[j]:
                    db += 1
            completed.append(lst[i])
            print(f'{lst[i]} - {db}db')


def main():
    lst = create_lst()
    func(lst)


if __name__ == '__main__':
    main()
