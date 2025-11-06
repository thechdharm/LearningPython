#remainder method - T-O(1), S-O(1)
def iseven_or_odd(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")

#Bitwise  - T-O(1), S-O(1) but faster as bitwise operations are faster
def iseven_or_odd2(num):
    if num & 1 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == '__main__':
    iseven_or_odd(30)
    iseven_or_odd(31)
    iseven_or_odd2(30)
    iseven_or_odd2(31)


