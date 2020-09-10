# python3

import sys
import threading

def form_tree(n, parents):
    tree = dict((i, []) for i in range(n))
    root = parents.index(-1)
    for index, parent in enumerate(parents):
        if parent == -1:
            pass
        else:
            tree[parent].append(index)
        # identify root
        # populate children of parents
    return tree


def compute_height(tree, root):
    # Replace this code with a faster implementation
    if root not in tree.keys():
        return 1
    for child in tree[root]:
        print(1 + compute_height(tree, child))

def traversal(tree, root):
    walk = [root]
    height = [1]
    max_height = 1
    cur_height = 0
    count = -1
    while len(walk) > 0:
        node = walk[-1]
        cur_height = height[-1] + 1
        walk.pop()
        height.pop()
        if node in tree.keys():
            for child in tree[node]:
                walk.append(child)
                height.append(cur_height)
                # print(node, height, sep=" | ")
            if cur_height>max_height:
                max_height = cur_height

    return max_height - 1

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = form_tree(n, parents)
    print(traversal(tree, parents.index(-1)))
    #print(compute_height(tree, parents.index(-1)))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
