from sys import stdin
import heapq


class HideAndSeek(object):

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.visited = [False for _ in range(100001)]

    def _next_step(self, cur):
        nexts = []
        if cur[1] > 0 and not self.visited[cur[1]-1]:
            nexts.append((cur[0]+1, cur[1]-1))
        if cur[1]+1 <= 100000 and not self.visited[cur[1]+1]:
            nexts.append((cur[0]+1, cur[1]+1))
        if cur[1]*2 <= 100000 and not self.visited[cur[1]*2]:
            nexts.append((cur[0], cur[1]*2))

        return nexts


    def get_shortest_path(self):
        h = [(0, self.n)]

        while h:
            top = heapq.heappop(h)
            if self.visited[top[1]]:
                continue
            if top[1] == self.k:
                return top[0]
            self.visited[top[1]] = True

            nexts = self._next_step(top)
            for nxt in nexts:
                top = heapq.heappush(h, nxt)
        return 0


if __name__ == '__main__':
    rd = stdin.readline
    n, k = tuple(map(int, rd().split()))
    has = HideAndSeek(n, k)
    print(has.get_shortest_path())
