def are_strings_permutations(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False


str1 = 'aaabbbccc'
str2 = 'abcacabc'
print(are_strings_permutations(str1, str2))
