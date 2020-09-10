# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        br = Bracket(next, i)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(br)

        if next in ")]}":
            # Process closing bracket, write your code here
            #if stack empty return False
            for j in range(1, len(opening_brackets_stack)):
                pos = len(opening_brackets_stack)-j
                if pos >= 0:
                    if are_matching(opening_brackets_stack[pos].char, next):
                        opening_brackets_stack.pop()
                    else:
                        #opening_brackets_stack.append(br)
                        return i+1#opening_brackets_stack.append(br)
                else:
                    return i + 1#opening_brackets_stack.append(br)

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack#[len(opening_brackets_stack)-1].position + 1



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
