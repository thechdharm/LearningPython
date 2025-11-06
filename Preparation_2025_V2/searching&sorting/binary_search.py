def binary_search_iter(arr, x, start, end):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] < x:
            start = mid +1
        elif arr[mid] > x:
            end = mid -1
        elif arr[mid] == x:
            return mid
    return -1

def binary_search_rec(arr, x, start, end):
    if start > end:
        return -1

    mid = start + (end-start)//2

    if arr[mid] < x:
        start = mid +1
    elif arr[mid] > x:
        end = mid -1
    elif arr[mid] == x:
        return mid
    return binary_search_rec(arr, x, start, end)

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    # result = binary_search_iter(arr, 4, 0, len(arr)-1)
    result = binary_search_rec(arr, 4, 0, len(arr)-1)
    print("reslt::", result)