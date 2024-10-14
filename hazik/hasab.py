def main():
    a = int(input('Kerem az "a" oldalt: '))
    b = int(input('Kerem az "b" oldalt: '))
    c = int(input('Kerem az "c" oldalt: '))
    print(f'a: {a}cm,b: {b}cm,c: {c}cm')

    V = a*b*c
    A = (a*b + a*c + b*c)*2
    print(f'V: {V}cm3\nA: {A}cm2')

if __name__ == '__main__':
    main()