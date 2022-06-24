"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""
"""Breadth First Search is based on Graph Traversal Algorithms"""


class Traversing:
    def __init__(self, input):
        self._visited_dfs = set()
        self._visited_bfs = list()
        self._queue = list()
        self._input = input

    def bfs(self, node):

        self._visited_bfs.append(node)
        self._queue.append(node)

        while self._queue:
            m = self._queue.pop(0)
            print(m, end=" ")
            for neighbour in self._input[m]:
                if neighbour not in self._visited_bfs:
                    self._visited_bfs.append(neighbour)
                    self._queue.append(neighbour)

    def dfs(self, node):
        if node not in self._visited_dfs:
            print(node, end=" ")
            self._visited_dfs.add(node)
            for neighbour in self._input[node]:
                self.dfs(neighbour)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    t = Traversing(graph)
    print('\n********************************************************************')
    print("Following is the Breadth-First Search", end='\n')
    t.bfs('5')
    print('\n********************************************************************')
    print("Following is the Depth-First Search", end='\n')
    t.dfs('5')
    print('\n********************************************************************')