def main():
    r = int(input("Kerem a gomb sugarat: "))
    V = 4 * r **3 * 3.14
    V_new = V / 3
    A =4 * r **2 * 3.14

    print(f"Felszine: {A}\nTerfogata: {V}")


if __name__ == '__main__':
    main()