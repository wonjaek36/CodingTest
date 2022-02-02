from sys import stdin


class VirusChecker(object):

    def __init__(self, n, m, edges):
        self._n = n
        self._m = m
        self._edges = edges
        self._visited = [False] * (n+1)

    def _explorer(self, n):
        if self._visited[n]:
            return 0

        self._visited[n] = True
        count = 0
        for i in self._edges[n]:
            count += self._explorer(i)
        return count + 1
    
    def check(self):
        return self._explorer(1)
            

if __name__ == '__main__':
    n = int(stdin.readline())
    m = int(stdin.readline())
    edges = {}
    for i in range(1, n+1):
        edges[i] = set()
        
    for _ in range(m):
        a, b = list(map(int, stdin.readline().split(' ')))
        edges[a].add(b)
        edges[b].add(a)

    vc = VirusChecker(n, m, edges)
    print(vc.check()-1)
        
