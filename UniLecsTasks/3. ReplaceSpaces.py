def replace_spaces(string, substitute):
    return substitute.join(string.split())

print(replace_spaces('abd skg afk', '%20'))
