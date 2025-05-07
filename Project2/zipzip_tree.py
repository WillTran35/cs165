# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file
from __future__ import annotations

from collections import deque
from typing import TypeVar
from dataclasses import dataclass
import math
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


@dataclass
class Rank:
    geometric_rank: int
    uniform_rank: int


class Node:
    def __init__(self, key, value, rank):
        self.key = key
        self.value = value
        self.rank = rank
        self.left = None
        self.right = None
        self.size = 1


class ZipZipTree:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.root = None  # should be a node
        self.count = -1
        # print(f"made zipzip cap - {self.capacity} size - {self.size} root = {self.root.key if self.root else None}" )

    def print_tree(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(
                f"Printing Key: {node.key}, Value: {node.value}, Rank: ({node.rank.geometric_rank}, {node.rank.uniform_rank})")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_random_rank(self) -> Rank:
        """# get_random_rank(): returns a random node rank, chosen independently from:
        # a geometric distribution of mean 1 and,
        # a uniform distribution of integers from 0 to log(capacity)^3 - 1 (log
        # capacity cubed minus 1)."""
        geometric = 0
        while random.random() < 0.5:
            geometric += 1
        max_uni = int(math.log(self.capacity) ** 3 - 1)
        uniform = random.randint(0, max(0, max_uni))
        return Rank(geometric, uniform)

    def compare_ranks(self, node1, node2):
        # return (node2.rank.geometric_rank > node1.rank.geometric_rank) or \
        # (node2.rank.geometric_rank == node1.rank.geometric_rank and node2.rank.uniform_rank > node1.rank.uniform_rank)
        """used for unzip funtion. returns true if node2 is greater than node1"""
        if node2.rank.geometric_rank != node1.rank.geometric_rank:
            return node2.rank.geometric_rank > node1.rank.geometric_rank
        if node2.rank.uniform_rank != node1.rank.uniform_rank:
            return node2.rank.uniform_rank > node1.rank.uniform_rank
        return node2.key < node1.key  # Prefer smaller keys on tie

    def compare_ranksZip(self, node1, node2) -> bool:

        if node1.rank.geometric_rank != node2.rank.geometric_rank:
            return node1.rank.geometric_rank > node2.rank.geometric_rank
        if node1.rank.uniform_rank != node2.rank.uniform_rank:
            return node1.rank.uniform_rank > node2.rank.uniform_rank
        return node1.key < node2.key  # Prefer smaller keys on tie

    def insert_recur(self, root, node):
        if not root:
            # print("returning node")
            return node

        # if equal:
        if self.compare_ranks(root, node):
            left, right = self.unzip(root, node.key)
            node.left = left
            node.right = right
            node.size = (left.size if left else 0) + (right.size if right else 0) + 1
            return node

        # if less than
        if node.key < root.key:
            root.left = self.insert_recur(root.left, node)
        #     if greater than
        else:
            root.right = self.insert_recur(root.right, node)

        root.size = (root.left.size if root.left else 0) + (root.right.size if root.right else 0) + 1
        return root

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        # print(key, val, rank)
        if rank is None:
            rank = self.get_random_rank()
        node = Node(key, val, rank)
        if self.root is None:
            self.root = node
            self.size += 1
            return self.root
        self.root = self.insert_recur(self.root, node)
        self.size += 1
        # print(f"!!made zipzip cap - {self.capacity} size - {self.size} root = {self.root}")

    def in_order_traversal(self, node, val):
        stack = []
        EPSILON = 1e-10
        # print(f"in order node: {node.value}")
        while stack or node:
            while node:
                stack.append(node)
                # print(f"outside33 {stack}")
                node = node.left
            # print(f"outside {node}")
            node = stack.pop()
            # print(f"outside3 {node}")
            if node.value + EPSILON >= val:
                # print("found a node")
                return node
            node = node.right
        return None

        #     node = node.left
        #     if not node:
        #         node = node.right
        #
        # left_result = self.in_order_traversal(node.left, val)
        # if left_result:
        #     return left_result
        # if node.value >= val:
        #     return node
        # return self.in_order_traversal(node.right, val)

    def insertForFirstFit(self, val):

        #     search for position to insert by checking size
        #     if it fits in a node, then we just subtract the size available,
        #     if we need to make a new node, we will make new node with key as the bin number and log it
        #       key is bin number, val is available capacity

        if not self.root:
            self.count += 1
            value = math.isclose(1, val, )
            node = Node(self.count, 1 - val, self.get_random_rank())
            self.root = self.insert_recur(self.root, node)
            self.size += 1
            print("if not self.root")
            return self.count, node.value
        else:
            #     traverse tree to find position
            temp = self.root
            node = self.in_order_traversal(temp, val)
            if node:
                # we have found spot to insert in current tree, we just need to subtract the current size and then
                # keep track of bucket
                node.value -= val
                return node.key, node.value
            else:
        #         make a new node and insert it
                self.count += 1
                new_node = Node(self.count, 1 - val, self.get_random_rank())
                self.root = self.insert_recur(self.root, new_node)
                self.size += 1
                return self.count, new_node.value



    def remove(self, key: KeyType):
        self.root = self.remove_recur(self.root, key)
        self.size = self.root.size if self.root else 0

    def zip(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if self.compare_ranksZip(left, right):
            left.right = self.zip(left.right, right)
            left.size = (left.left.size if left.left else 0) + (left.right.size if left.right else 0) + 1
            return left

        else:
            right.left = self.zip(left, right.left)
            right.size = (right.left.size if right.left else 0) + (right.right.size if right.right else 0) + 1
            return right

    def remove_recur(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self.remove_recur(root.left, key)
        elif key > root.key:
            root.right = self.remove_recur(root.right, key)
        else:
            return self.zip(root.left, root.right)

        root.size = (root.left.size if root.left else 0) + (root.right.size if root.right else 0) + 1
        return root

    def find(self, key: KeyType) -> ValType:
        curr = self.root
        # print(f"THIS IS CURR {curr.key}" )
        while curr:
            # print("in while loop")
            if curr.key == key:
                return curr.value
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return curr.value if curr else None

    def get_size(self) -> int:
        return self.root.size

    def get_height(self) -> int:
        return self.get_height_recur(self.root)

    def get_height_recur(self, root):
        if not root:
            return -1
        return 1 + max(self.get_height_recur(root.left), self.get_height_recur(root.right))

    def get_depth(self, key: KeyType):
        curr = self.root
        count = 0
        while curr:
            if curr.key == key:
                return count
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
            count += 1
        return count

    def unzip(self, root, key):
        """"Split a subtree into left and right subtrees based on key."""
        if not root:
            return None, None

        if key < root.key:
            left, right = self.unzip(root.left, key)
            root.left = right
            root.size = (root.left.size if root.left else 0) + (root.right.size if root.right else 0) + 1
            return left, root
        else:
            left, right = self.unzip(root.right, key)
            root.right = left
            root.size = (root.left.size if root.left else 0) + (root.right.size if root.right else 0) + 1
            return root, right

# feel free to define new methods in addition to the above
# fill in the definitions of each required member function (above),
# and for any additional member functions you define
