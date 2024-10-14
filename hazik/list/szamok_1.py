import random
import math

def main():
    lst = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
           100, 67, 22, 8, -78, -6]

    print('1.feladat:')
    masolat = lst.copy()
    masolat.sort(reverse=True)
    for i in masolat:
        num = i ** 3
        if num % 2 == 0:
            print(num)



if __name__ == '__main__':
    main()