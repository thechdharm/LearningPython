def interative(li):
    result = []
    for i in range(0, len(li)):
        if i % 2 == 0:
            result.append(str(li[i]))
    print(" ".join(result))
    

def recursive(li, start=0, res=[]):
    if start < len(li):
        res.append(str(li[start]))
        return recursive(li, start+ 2, res)
    else:
        return res
    


if __name__ == '__main__':
    arr = [30, 41, 52, 63, 75, 81]
    interative(arr)
    result = recursive(arr, 0, [])
    print(" ".join(result))
    # print("result::", result)
