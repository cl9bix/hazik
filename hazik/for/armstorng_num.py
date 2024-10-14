import math


def main():
    for n in range(100,999):
        get_first_element = math.pow(math.floor(n / 100),3)
        get_second_element = math.pow(math.floor(n % 100)//10,3)
        get_third_element = math.pow(math.floor(n % 10),3)
        arm_num = get_first_element + get_second_element + get_third_element
        if arm_num == n:
            print(round(arm_num))


if __name__ == '__main__':
    main()
