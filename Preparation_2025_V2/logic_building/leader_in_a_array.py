def sol1(li):
    leaders = []
    max_right = 0
    for i in range(len(li)-1, -1, -1):
        if li[i] > max_right:
            max_right = li[i]
            leaders.append(str(max_right))
    return leaders

if __name__ == '__main__':
    # arr = [30, 41, 52, 63, 75, 81, 3, 4, 0]
    arr = [16, 17, 4, 3, 5, 2]
    result = sol1(arr)
    print(" ".join(result))