#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def inOrderTraversal(tree, ind, keys):
    if ind == -1:
        return
    if not IsBinarySearchTree(tree, ind, []):
        return False
    keys.append(tree[ind][0])
    inOrderTraversal(tree, tree[ind][1], keys)
    inOrderTraversal(tree, tree[ind][2], keys)

def IsBinarySearchTree(tree, ind, res):
    # Implement correct algorithm here
    if tree == []:
        return True
    # if ind == -1:
    #     return True
    left = []
    if inOrderTraversal(tree, tree[ind][1], left) == False:
        return False
    right = []
    if inOrderTraversal(tree, tree[ind][2], right) == False:
        return False

    # print(left)
    # print(right)
    if left:
        for el in left:
            if el >= tree[ind][0]:
                return False
    if right:
        for el in right:
            if el < tree[ind][0]:
                return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    res = []
    if IsBinarySearchTree(tree, 0, res):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
