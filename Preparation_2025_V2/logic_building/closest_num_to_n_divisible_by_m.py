#no extra variable method - T-O(1), S-O(1)
def closest_number(a,b):
    re = a % b
    print(a-re)
    

if __name__ == '__main__':
    closest_number(3000, 31)
    closest_number(13, 4)