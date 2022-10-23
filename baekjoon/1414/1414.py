from sys import stdin
import heapq


class HelpingOthers(object):

    def __init__(self, n, edges):
        self.n = n
        self.visited = [False for _ in range(n)]
        self.edges = self._change_value(edges)

    def _change_value(self, edges):
        e = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if 'a' <= edges[i][j] <= 'z':
                    e[i][j] = ord(edges[i][j])-ord('a')+1
                elif 'A' <= edges[i][j] <= 'Z':
                    e[i][j] = ord(edges[i][j])-ord('A')+27
        return e
    
    def _get_length(self, a, b):
        if a == 0 and b == 0:
            return -1
        if a == 0:
            return b
        if b == 0:
            return a
        return min(a, b)

    def get_remains(self):
        h = [(0, 0)]

        mst = 0
        connects = 0
        while h:
            val, cur = heapq.heappop(h)
            if self.visited[cur]:
                continue
            self.visited[cur] = True
            mst += val
            connects += 1

            for i in range(n):
                if self.visited[i]:
                    continue

                val = self._get_length(self.edges[cur][i],
                                       self.edges[i][cur])
                if val == -1:
                    continue
                heapq.heappush(h, (val, i))

        if connects >= self.n:
            return sum(map(sum, self.edges))-mst
        return -1


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    edges = [list(rd().rstrip()) for _ in range(n)]

    ho = HelpingOthers(n, edges)
    print(ho.get_remains())


