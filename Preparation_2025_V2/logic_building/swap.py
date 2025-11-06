#no extra variable method - T-O(1), S-O(1)
def swap(a,b):
    print("Initial values:")
    print("a: ", a)
    print("b: ", b)

    # b = (a+b) - (a = b)
    # a = a + b - (b = a) # This works in other languages
    a = a + b - (b := a)
    print("After swap values:")
    print("a: ", a)
    print("b: ", b)
    

#recursive - T-O(1), S-O(1)
def swap_v2(num, i=1):
    pass

if __name__ == '__main__':
    swap(30, 60)
    swap(31)
    # swap_v2(30)
    # swap_v2(31)