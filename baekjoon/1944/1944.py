from sys import stdin
from collections import deque
import heapq
from functools import reduce


class KeyRobot(object):

    INT_MAX = 0x7fffffff

    def __init__(self, mp, m):
        self._nodes = m+1
        self._mp = mp
        self._ms = len(mp)
        self._gp = [[self.INT_MAX]*self._nodes for _ in range(self._nodes)]
        self._entity_index = {}
        self._construct_graph()

    def _find_robot(self):
        map_size, mp = self._ms, self._mp
        for i in range(1, map_size-1):
            for j in range(1, map_size-1):
                if mp[i][j] == 'S':
                    return (i, j)

        return (-1, -1)

    def _find_keys(self):
        map_size, mp = self._ms, self._mp
        keys = []
        for i in range(1, map_size-1):
            for j in range(1, map_size-1):
                if mp[i][j] == 'K':
                    keys.append((i, j))

        return keys

    def _bfs(self, x, y, idx):
        _visited = [[False]*self._ms for _ in range(self._ms)]
        _direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        q.append((x, y, 0))

        while q:
            cx, cy, cs = q.popleft()

            if self._mp[cx][cy] == '1':
                continue
            if _visited[cx][cy]:
                continue
            _visited[cx][cy] = True

            if (cx, cy) in self._entity_index:
                ci = self._entity_index[(cx, cy)]
                self._gp[idx][ci] = self._gp[ci][idx] = cs

            for dx, dy in _direction:
                q.append((cx+dx, cy+dy, cs+1))

    def _construct_graph(self):
        rx, ry = self._find_robot()
        assert rx != -1 and ry != -1
        self._entity_index[(rx, ry)] = 0

        keys = self._find_keys()
        for idx, k in enumerate(keys):
            self._entity_index[k] = idx+1
        
        for (x, y), v in self._entity_index.items():
            self._bfs(x, y, v)

    def _add_edges(self,
                   node,
                   hp,
                   visited):
        for next_node, edges_value in enumerate(self._gp[node]):
            if visited[next_node]:
                continue
            if edges_value == self.INT_MAX:
                continue
            heapq.heappush(hp, (edges_value, next_node))

        return hp

    def search_keys(self):
        visited, hp = [False]*self._nodes, []
        self._add_edges(0, hp, visited)

        weight = 0
        while hp:
            edge, node = heapq.heappop(hp)
            if visited[node]:
                continue

            visited[node] = True
            weight += edge
            self._add_edges(node, hp, visited)

        all_visited = reduce(lambda acc, v: acc and v, visited, True)
        return weight if all_visited else -1


if __name__ == '__main__':
    rd = stdin.readline
    n, m = list(map(int, rd().split(' ')))
    mp = [rd() for _ in range(n)]

    kr = KeyRobot(mp, m)
    print(kr.search_keys())
