# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

"""
LRU (Least Recently Used) Cache is a type of caching Algorithm.

Each Cache has a limited capacity to store data.

We will be using Following Approach for Implementing LRU Cache.

1) Doubly Linked List:
    Doubly Linked List is easy to manipulate since both the starting and the next position is present you can easily 
    remove any node from between.
2) Hashing Table:
    Hashing Table is used to maintain the data and check whether the value is present in Linked List or Not.
    
For Hashing Table I'll be using Dictionary in Python.
"""

from collections import OrderedDict

class Node:
    def __init__(self, node_key, value):
        self.node_key = node_key
        self.value = value
        self.next_node = None
        self.prev_node = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.current_size = 0
        self.hash_table = OrderedDict()

    def remove_node(self, node):
        node_after = node.next_node
        node_before = node.prev_node
        node_before.next_node = node_after
        node_after.prev_node = node_before

    def add_node(self, node):
        prev_node_tail = self.tail.prev_node
        prev_node_tail.next_node = node
        node.prev_node = prev_node_tail
        node.next_node = self.tail
        self.tail.prev = node

    def get(self, node_key: int) -> int:
        if node_key not in self.hash_table:
            return -1
        node = self.hash_table[node_key]
        node_val = node.value
        self.remove_node(node)
        self.add_node(node)
        return node_val

    def put(self, node_key: int, new_val: int) -> None:
        if node_key in self.hash_table:
            node = self.hash_table[node_key]
            node.val = new_val
            self.remove_node(node)
            self.add_node(node)
        else:
            if self.current_size >= self.capacity:
                lru_node = self.head.next_node
                del self.hash_table[lru_node.node_key]
                self.remove_node(lru_node)
                self.current_size -= 1

            new_node = Node(node_key, new_val)
            self.hash_table[node_key] = new_node
            self.add_node(new_node)
            self.current_size += 1


if __name__ == '__main__':
    cache = LRUCache(5)
    print(cache.hash_table)
    cache.put(1, 100)
    print(cache.hash_table)
    cache.put(2, 200)
    print(cache.hash_table)
    cache.put(3, 500)
    print(cache.hash_table)
    cache.put(5, 1100)
    print(cache.hash_table)
    cache.put(0, 1200)
    print(cache.hash_table)
    print(cache.get(2))
    print(cache.hash_table)
    print(cache.get(0))
    print(cache.hash_table)
    cache.put(10, 1100)
    print(cache.hash_table)
    cache.put(111, 1100)
    print(cache.hash_table)
    cache.put(132, 1100)
    print(cache.hash_table)
