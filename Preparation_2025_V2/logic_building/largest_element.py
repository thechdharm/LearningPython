def interative(li):
    result = float("-inf")
    for i in range(0, len(li)):
        result = max(li[i], result)
    return result
    

def recursive(li, i):
    if i == len(li)-1:
        return li[i]
    rec_max = recursive(li, i+1)
    return max(rec_max, li[i])
    


if __name__ == '__main__':
    arr = [30, 41, 52, 63, 75, 81]
    result = interative(arr)
    print("result::", result)
    result = recursive(arr, 0)
    print("result::", result)
