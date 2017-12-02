# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import sys

from common.Tree import TreeNode

sys.setrecursionlimit(1500)


def swap(k, node, depth):
    if not node:
        return None
    swap(k, node.left, depth + 1)
    swap(k, node.right, depth + 1)

    if depth % k == 0:
        temp = node.left
        node.left = node.right
        node.right = temp


def print_in_order(node):
    if not node:
        return None

    print_in_order(node.left)
    print(node.value, end=" ")
    print_in_order(node.right)


input_len_for_tree = int(input())
nodes = [None] * (input_len_for_tree + 1)

for i in range(1, input_len_for_tree + 1):
    nodes[i] = TreeNode(i)

for i in range(1, input_len_for_tree + 1):
    left_and_right = str(input()).split(" ")
    left = int(left_and_right[0])
    right = int(left_and_right[1])

    nodes[i].left = None if left == -1 else nodes[left]
    nodes[i].right = None if right == -1 else nodes[right]

input_len_for_swap = int(input())

for i in range(0, input_len_for_swap):
    k = int(input())
    swap(k, nodes[1], 1)
    print_in_order(nodes[1])
    print("")
