def generate_all_subarrays_iterative(arr):
    result = []
    for ch_idx in range(len(arr)):
        for ss_index in range(ch_idx, len(arr)):
            result.append(arr[ch_idx: ss_index +1])
    return list(result)

def generate_all_subarrays_rec(arr):
    if len(arr) == 1:
        result_subarrays = [[arr[0]]]
        # print("result_subarrays::", result_subarrays)
        return result_subarrays

    
    
    result = []
    remainig_array_subarrays = generate_all_subarrays_rec(arr[1:])
    
    result.extend(remainig_array_subarrays)

    for r_s in remainig_array_subarrays:
        # print("====r_s:::", r_s)
        # print("====arr[0: 1]:::", arr[0: 1])
        result.append(r_s)
        result.append(arr[0: 1]+ r_s)
    return result

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    # result = generate_all_subarrays_iterative(arr)
    result = generate_all_subarrays_rec(arr)
    for idx, val in enumerate(result):
        print("Subarray No. - {} is {}".format(idx+1, " ".join(list(map(str, val)))))