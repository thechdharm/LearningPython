#iterative method - T-O(log10n), S-O(1)
def prime1(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

import math
def prime2(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def prime3(num):
    if num == 1 or num == 3 or num == 2:
        return True
    for i in range(5, num, 6):
        if num % i ==0:
            return False
    return True


def prime4(num):
    if num == 1 or num == 3 or num == 2:
        return True
    for i in range(5, int(math.sqrt(num)), 6):
        if num % i ==0:
            return False
    return True

if __name__ == '__main__':
    # print(prime1(int(input())))
    # print(prime2(int(input())))
    # print(prime3(int(input())))
    print(prime4(int(input())))