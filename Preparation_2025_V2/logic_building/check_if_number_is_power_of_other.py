
def is_power(num, num2):
    if num == 1:
        return num2 ==1
    
    pow = 1
    


import math
def is_power2(num, num2):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def is_power3(num, num2):
    if num == 1 or num == 3 or num == 2:
        return True
    for i in range(5, num, 6):
        if num % i ==0:
            return False
    return True


if __name__ == '__main__':
    print(is_power(int(input())))
    print(is_power2(int(input())))
    print(is_power3(int(input())))