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
            # если стек пуст
            if not opening_brackets_stack:
                return i+1
            # Process closing bracket, write your code here
            if are_matching(opening_brackets_stack[-1].char, next):
                opening_brackets_stack.pop()
            else:
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position+1
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
