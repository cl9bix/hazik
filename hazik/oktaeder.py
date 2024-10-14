import math


def main():
    alkoto = float(input("Kerem az oktaeder alkotojat: "))

    A = 2 * math.sqrt(3) * alkoto ** 2

    V = (math.sqrt(2) / 3) * alkoto ** 3

    R = (math.sqrt(2) / 2) * alkoto
    r = (math.sqrt(6) / 6) * alkoto
    print("Felszin (A):", A)
    print("Terfogat (V):", V)
    print("r (r):", r)
    print("R (R):", R)


if __name__ == '__main__':
    main()
