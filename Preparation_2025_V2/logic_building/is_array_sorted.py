def is_sorted(li, n):
    if n == 0 or n==1:
        return True
    return li[n-1] > li[n-2] and is_sorted(li, n-1)
    

if __name__ == '__main__':
    arr = [16, 17, 4, 3, 5, 2]
    result = is_sorted(arr, len(arr))
    print(result)