'''
All the content presented to us in textual form can be visualized as nothing but just strings.

Tries:

Tries are an extremely special and useful data-structure that are based on the prefix of a string. They are used to
represent the “Retrieval” of data and thus the name Trie.

Prefix : What is prefix:

The prefix of a string is nothing but any n letters n <= |S| that can be considered beginning strictly from the starting
 of a string. For example , the word “abacaba” has the following prefixes:

A Trie is a special data structure used to store strings that can be visualized like a graph. It consists of nodes and
edges. Each node consists of at max 26 children and edges connect each parent node to its children. These 26 pointers
are nothing but pointers for each of the 26 letters of the English alphabet A separate edge is maintained for every edge.

Strings are stored in a top to bottom manner on the basis of their prefix in a trie. All prefixes of length 1 are stored
at until level 1, all prefixes of length 2 are sorted at until level 2 and so on.
'''

import collections

Trie = lambda: collections.defaultdict(Trie)
END = 'is_end'


class CRUDTrie_2:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        word = word.lower()
        curr = self.root
        for char in word:
            curr[char] = Trie()
            curr[END] = False
            curr = curr[char]
        curr[END] = True

    def search(self, word):
        word = word.lower()
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return True


if __name__ == '__main__':
    insert = ['Cat', 'Mouse', 'Rat', 'bAt']
    search = ['Ca', 'DB', 'MOUSE']
    c = CRUDTrie_2()
    for e in insert:
        c.insert(e)

    for f in search:
        print(c.search(f))
