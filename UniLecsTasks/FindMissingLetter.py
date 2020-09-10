arr = ['a', 'b', 'c', 'd', 'e', 'g']

first_letter_code = ord(arr[0])

for char_ind in range(first_letter_code, first_letter_code + len(arr)):
    if arr[char_ind - first_letter_code] != chr(char_ind):
        print(chr(char_ind))
        break
