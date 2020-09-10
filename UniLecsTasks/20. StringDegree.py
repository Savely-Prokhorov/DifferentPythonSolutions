def str_degree(str, k):
    subsets_len = len(str) // abs(k)
    if subsets_len == len(str) / abs(k):
        subsets = []
        for i in range(0, len(str), 3):
            subsets.append(str[i:i+3])
        count = 0
        for i in range(subsets_len - 1):
            if subsets[i] == subsets[i+1]:
                count += 1
        if count == subsets_len - 1:
            return subsets[0]
    return "Error"


str = 'AbcdAbccAbcd'
k = -3
print(str_degree(str, k))
