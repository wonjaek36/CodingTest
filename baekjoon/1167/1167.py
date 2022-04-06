from sys import stdin


class TreeDiameter(object):

    def __init__(self, tree):
        self._tree = tree
        self._visited = None

    def get_diameter(self):
        self._visited = [False]*(len(self._tree)+1)        
        n, _ = self._find_longest_distance(1, 0)
        self._visited = [False]*(len(self._tree)+1)
        _, d = self._find_longest_distance(n, 0)
        return d

    def _find_longest_distance(self, c, c_dis):
        if self._visited[c]:
            return c, 0

        self._visited[c] = True
        max_dis = (c, c_dis)
        for nxt, dis in zip(self._tree[c][::2],
                            self._tree[c][1::2]):
            t = self._find_longest_distance(nxt, c_dis+dis)
            max_dis = max(max_dis, t, key=lambda x: x[1])

        return max_dis

    
if __name__ == '__main__':
    n = int(stdin.readline())
    nodes = {i: [] for i in range(1, n+1)}
    for _ in range(n):
        i, *ed = stdin.readline().rstrip().split(' ')
        nodes[int(i)] = list(map(int, ed))
    
    td = TreeDiameter(nodes)
    print(td.get_diameter())
