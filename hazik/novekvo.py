def main():
    a = int(input('Kerem az 1. szamot: '))
    b = int(input('Kerem az 2. szamot: '))
    c = int(input('Kerem az 3. szamot: '))

    if a >= b and a >= c:
        if b >= c:
            print(c, b, a)
        else:
            print(b, c, a)
    elif b >= a and b >= c:
        if a >= c:
            print(c, a, b)
        else:
            print(a, c, b)
    elif c >= a and c >= b:
        if a >= b:
            print(b, a, c)
        else:
            print(a, b, c)


if __name__ == '__main__':
    main()
