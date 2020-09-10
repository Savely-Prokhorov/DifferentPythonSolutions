def is_balanced(s):
    ob = ['(', '{']  # opening braces
    cb = [')', '}']  # closing braces

    stack = []
    for el in s:
        if el in ob:
            stack.append(el)
        if el in cb:
            try:
                if stack != [] and ob.index(stack[len(stack)-1]) == cb.index(el):
                    stack.pop()
                else:
                    stack.append(el)
            except ValueError:
                pass
    if stack != []:
        return False
    return True

print(is_balanced('({(}){})'))

