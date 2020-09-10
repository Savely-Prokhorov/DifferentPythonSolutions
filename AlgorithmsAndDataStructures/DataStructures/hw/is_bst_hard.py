#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def inOrderTraversal(tree, ind, keys, part):
    if ind == -1:
        return

    # part: either 1 (left) or 2(right)

    # print(keys)
    # if left child == parent
    if tree[ind][1] != -1: #if left child exists
        if tree[ind][0] == tree[tree[ind][1]][0]:
            tree[tree[ind][1]][0] += 1
    inOrderTraversal(tree, tree[ind][1], keys, 1)
    keys.append((tree[ind][0], part))
        # print(tree)
    inOrderTraversal(tree, tree[ind][2], keys, 2)


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree:
        return True

    keys = []
    inOrderTraversal(tree, 0, keys, 0)
    # print(keys)

    for i in range(len(keys)-1):
        if keys[i][0] > keys[i+1][0]:
            return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
