from dfs import DFS

import unittest

class TestStringMethods(unittest.TestCase):

    def test_dfs(self):
        matrix = [
        [0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
        ]

        G = DFS(matrix=matrix)
        print(G)    


if __name__ == '__main__':
    unittest.main()