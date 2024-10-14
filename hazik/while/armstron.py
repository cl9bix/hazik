def main():
    n = 100
    print("Armstrong szamok: ")
    while n < 999:
        if (n // 100)**3 + ((n // 10) % 10)**3 + (n % 10)**3 == n:
            print(n,end=' ')
        n += 1



if __name__ == '__main__':
    main()