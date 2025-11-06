#iterative method - T-O(1), S-O(1)
def multiplication_table(num):
    print("Starting Table")
    for i in range(1,11):
        print(num*i)
    print("End Table")

#recursive - T-O(1), S-O(1)
def multiplication_table_v2(num, i=1):
    if i > 10:
        return
    # multiplication_table_v2(num)
    print(i*num)
    i = i +1
    multiplication_table_v2(num, i)
    return 

if __name__ == '__main__':
    # multiplication_table(30)
    # multiplication_table(31)
    multiplication_table_v2(30)
    multiplication_table_v2(31)