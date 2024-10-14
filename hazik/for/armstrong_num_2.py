import math


def main():
    for n in range(1000,10000):
        get_first_element = math.pow(math.floor(n / 1000),4)
        get_second_element = math.pow(math.floor((n % 1000)//100),4)
        get_third_element = math.pow(math.floor(n % 100) // 10,4)
        get_fourth_element = math.pow(n % 10,4)
        arm_num = get_first_element + get_second_element + get_third_element + get_fourth_element
        if arm_num == n:
            print(round(arm_num))


if __name__ == '__main__':
    main()
