from sys import stdin
from collections import deque


class TreeParent(object):

    def __init__(self, n, conns):
        self._conns = conns
        self._n = n
        self._parent = [-1]*(n+1)

    def search_parent(self):
        q = deque([1])
        self._parent[1] = 0
        while q:
            s = q.popleft()
            s_conns = self._conns[s]
            children = list(filter(
                lambda x: self._parent[x] == -1,
                s_conns))

            for child in children:
                self._parent[child] = s

            q.extend(children)
        return self._parent[2:]


if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    conns = {}
    for _ in range(n-1):
        a, b = list(map(
            int, stdin.readline().rstrip().split(' ')))
        if a not in conns:
            conns[a] = []
        if b not in conns:
            conns[b] = []

        conns[a].append(b)
        conns[b].append(a)

    tp = TreeParent(n, conns)
    parents = tp.search_parent()
    print('\n'.join(map(str, parents)))
