from sys import stdin
import sys
sys.setrecursionlimit(10**6)


class TreeDiameter(object):

    def __init__(self, n, tree):
        self._n = n
        self._tree = tree
        self._visited = None

    def get_diameter(self):
        self._visited = [-1]*(n+1)
        fn, dis = self._get_longest_path(1, 0)
        self._visited = [-1]*(n+1)
        sn, dis = self._get_longest_path(fn, 0)

        return dis

    def _get_longest_path(self, n, n_dis):
        if self._visited[n] != -1:
            return 0, 0
        self._visited[n] = n_dis

        mmd = n_dis
        mmn = n
        res = [(mmn, mmd)]
        res.extend([self._get_longest_path(nn, n_dis+nd)
                    for nn, nd in self._tree[n]])
        mmn, mmd = max(res, key=lambda x: x[1])

        return mmn, mmd


if __name__ == '__main__':
    n = int(stdin.readline())
    edges = {i+1:[] for i in range(n)}
    for _ in range(n-1):
        a, b, v = list(map(
            int, stdin.readline().split(' ')))
        edges[a].append((b, v))
        edges[b].append((a, v))

    td = TreeDiameter(n, edges)
    print(td.get_diameter())
    
