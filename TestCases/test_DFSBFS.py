import unittest
from Algorithms.Search_Algorithms.DFS import DepthFirstSearch
from Algorithms.Search_Algorithms.BFS import BreadthFirstSearch

d = DepthFirstSearch()
b = BreadthFirstSearch()
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(d.dfsearch(graph, visited, 'A', 'K'), 0)

    def test2(self):
        self.assertEqual(b.bfsearch(graph, 'A', 'C'), 1)


if __name__ == '__main__':
    MyTestCase.test1()
    MyTestCase.test2()
