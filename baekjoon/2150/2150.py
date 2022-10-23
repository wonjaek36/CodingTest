from sys import stdin
import sys
sys.setrecursionlimit(10**6)


class SCC(object):

    def __init__(self, v, e, edges):
        self.v = v
        self.e = e
        self.edges = edges
        self.visited = [-1 for _ in range(v+1)]
        self.visited_count = 0
        self.connections = None

        self.stack = []
        self.top = -1
        self.sccs = []
        self.is_sccs = [False for _ in range(v+1)]

    def _stack_pop(self):
        self.top -= 1
        return self.stack.pop()

    def _stack_push(self, c):
        self.top += 1
        self.stack.append(c)

    def _traverse(self, c):
        if self.visited[c] != -1:
            if self.is_sccs[c]:
                return self.v+1
            return self.visited[c]

        self.visited_count += 1
        self.visited[c] = self.visited_count
        self._stack_push(c)

        min_v = self.visited_count
        assert type(self.connections) is list
        assert type(self.connections[c]) is list
        for nxt in self.connections[c]:
            min_v = min(min_v, self._traverse(nxt))

        if not self.is_sccs[c] and min_v == self.visited[c]:
            p = self.top
            while self.stack[p] != c and p >= 0:
                p -= 1
            assert p != -1

            scc = []
            vertex = -1
            while vertex != c:
                vertex = self._stack_pop()
                self.is_sccs[vertex] = True
                scc.append(vertex)
            self.sccs.append(sorted(scc))

        return min_v

    def _make_linked_list(self):
        self.connections = [[] for _ in range(self.v+1)]
        for a, b in self.edges:
            self.connections[a].append(b)

    def get_sccs(self):
        self._make_linked_list()
        for i in range(1, self.v+1):
            if self.visited[i] == -1:
                self._traverse(i)
        return sorted(self.sccs)


if __name__ == '__main__':
    rd = stdin.readline
    v, e = list(map(int, rd().split()))
    edges = [list(map(int, rd().split())) for _ in range(e)]
    scc = SCC(v, e, edges)

    sccs = scc.get_sccs()
    print(len(sccs))
    for scc in sccs:
        print(*scc, -1)
