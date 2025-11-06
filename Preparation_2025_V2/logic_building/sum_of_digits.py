#iterative method - T-O(log10n), S-O(1)
def sum_of_digits(num):
    result = 0
    while num > 0:
        print("num:", num)
        remainder = num % 10
        print("remainder:", remainder)
        result = result * 10 + remainder
        print(int(result))
        num = num // 10


if __name__ == '__main__':
    sum_of_digits(31741)