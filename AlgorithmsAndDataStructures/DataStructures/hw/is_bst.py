#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def postOrderTraversal(tree, ind, keys):
    if ind == -1:
        return

    postOrderTraversal(tree, tree[ind][1], keys)
    postOrderTraversal(tree, tree[ind][2], keys)
    if tree[ind][1] == tree[ind][2]:
        keys.append(True)
    else:
        if tree[ind][1] != -1:
            if tree[tree[ind][1]][0] < tree[ind][0]:
                if tree[ind][2] != -1:
                    if tree[tree[ind][2]][0] > tree[ind][0]:
                        keys.append(True)
                    else:
                        keys.append(False)
                else:
                    keys.append(True)
            else:
                keys.append(False)
        else:
            if tree[tree[ind][2]][0] > tree[ind][0]:
                keys.append(True)
            else:
                keys.append(False)

def inOrderTraversal(tree, ind, keys, part):
    if ind == -1:
        return

    # part: either 1 (left) or 2(right)
    part = 1
    inOrderTraversal(tree, tree[ind][part], keys, part)
    keys.append((tree[ind][0], part))
    part = 2
    inOrderTraversal(tree, tree[ind][part], keys, part)

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree or len(tree)==1:
        return True

    if len(tree)==2:
        if tree[0][1] != -1:
            if tree[1][0] >= tree[0][0]:
                return False
        else:
            if tree[1][0] < tree[0][0]:
                return False

    keys = []
    inOrderTraversal(tree, 0, keys)
    if len(keys) >= 3:
        for i in range(len(keys)-2):
            if keys[i] > keys[i+1] or keys[i]==keys[i+1] and keys[i+1] <= keys[i+2]:
                return False
        # checking last leaves
        for i in range(len(keys)-2, len(keys)-1):
            if keys[i] > keys[i+1]:
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
