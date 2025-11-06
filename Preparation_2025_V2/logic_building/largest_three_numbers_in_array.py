def lg_3_numbers(li):
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")
    for i in li:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second and i != first:
            third = second
            second = i
        elif i > third and i != first and i != second:
            second = i
    return list(map(str, [first, second, third]))


if __name__ == '__main__':
    arr = [30, 41, 52, 63, 75, 81]
    result = lg_3_numbers(arr)
    print(" ".join(result))