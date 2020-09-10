# python3

import sys
import threading


# def find_max(arr):
#     max_i = 0
#     res = []
#     for i in range(len(arr)):
#         if arr[i] > arr[max_i]:
#             max_i = i
#     for i in range(len(arr)):
#         if arr[i] == arr[max_i]:
#             res.append(i)
#     return res


def get_subtrees(n, root, parents):
    res = []
    for i in range(n):
        if parents[i] == root:
            res.append(i)
    return res

def compute_height(n, root_ind, parents):
    # Replace this code with a faster implementation
    if not parents:
        return 0
    # try:
    else:
        subtrees = get_subtrees(n, root_ind, parents)
        args = [compute_height(n, root, parents) for root in subtrees]
        # if subtrees is not []:
        #     print(subtrees)
        #     print(args)
        if args:
            return 1 + max(args)
        else:
            return 1
    # except ValueError:
    #     return 0

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents.index(-1), parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
