def generate_ind_list(i, s_length):
    # если число нечетное
    if i % 2 == 0:
        arr = [i for i in range(0, s_length, 2)]
    # если четное
    else:
        arr = [i for i in range(1, s_length, 2)]
    return arr


def are_siblings(s1, s2):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            # если данный символ есть во второй строке
            if s1[i] in s2:
                # на местах той же четности ищем тот же символ
                count = 0
                for j in generate_ind_list(i, len(s2)):
                    if s1[i] == s2[j]:
                        count += 1
                if count == 0:
                    return False
    else:
        return False
    return True


print(are_siblings('abcdef', 'bcdaef'))
