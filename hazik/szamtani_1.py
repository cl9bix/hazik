def main():
    a = int(input("Kerem az elso elemet: "))
    d = int(input("Kerem a sorozat differenciaját: "))
    n = int(input("Hanyadik tag:? "))

    nth_term = a + (n - 1) * d

    sum_n = n * (a + nth_term) / 2

    print(f"A {n}. tag: {nth_term}")
    print(f"A sorozat osszege az elso {n} tagig: {sum_n}")


if __name__ == '__main__':
    main()
