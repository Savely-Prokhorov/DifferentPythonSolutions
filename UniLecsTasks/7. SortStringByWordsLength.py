in_str = 'Hello dear sir Adolfer Tannenbaum'

words = in_str.split()

for i in range(0, len(words) - 1):
    for j in range(0, len(words) - 1):
        if len(words[j + 1]) > len(words[j]):
            swap = words[j + 1]
            words[j + 1] = words[j]
            words[j] = swap

out_str = ' '.join(words)
print(out_str)
