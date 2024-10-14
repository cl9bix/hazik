import math


def main():
    alkoto = float(input("Kerem az ikozaeder alkotojat: "))

    A = 5 * math.sqrt(3) * alkoto ** 2

    V = (5 / 12) * (3 + math.sqrt(5)) * alkoto ** 3

    print("Felszin (A):", A)
    print("Terfogat (V):", V)


if __name__ == '__main__':
    main()
