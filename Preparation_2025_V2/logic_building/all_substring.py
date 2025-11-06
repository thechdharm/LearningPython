def generate_all_substring_iterative(st):
    result = set()
    for ch_idx in range(len(st)):
        for ss_index in range(ch_idx, len(st)):
            result.add(st[ch_idx: ss_index+1])
    return list(result)


def generate_all_substring_rec(st):
    if len(st) == 1:
        return st
    
    result = []
    remainig_strings = generate_all_substring_rec(st[1:])
    result.extend(remainig_strings)

    for r_s in remainig_strings:
        result.append(r_s)
        result.append(st[0: 1]+ r_s)
    return result


if __name__ == '__main__':
    a = input("Enter your string!")
    # result = generate_all_substring_iterative(a)
    result = generate_all_substring_rec(a)
    for idx, val in enumerate(result):
        print("Substring No. - {} is {}".format(idx+1, val))