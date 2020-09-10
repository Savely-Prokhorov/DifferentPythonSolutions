#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def inOrderTraversal(tree, ind):
    if ind == -1:
        return True

    left = IsBinarySearchTree(tree, tree[ind][1])
    right = IsBinarySearchTree(tree, tree[ind][2])
    if left and right:
        return True
    return False


def IsBinarySearchTree(tree, ind):
    # Implement correct algorithm here
    if tree == []:
        return True
    if ind == -1:
        return True

    left = inOrderTraversal(tree, tree[ind][1])
    right = inOrderTraversal(tree, tree[ind][2])
    print(left)
    print(right)

    # if left is not None:
    #     for el in left:
    #         if el >= tree[0][0]:
    #             return False
    # if right is not None:
    #     for el in right:
    #         if el <= tree[0][0]:
    #             return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree, 0):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
