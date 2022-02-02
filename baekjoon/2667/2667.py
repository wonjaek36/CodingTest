from sys import stdin


class NumberingComplex(object):

    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._visited = [[0]*n for _ in range(n)]

    def _fill_complex(self, x, y, number):
        d = NumberingComplex.d
        if self._m[x][y] != '1' or self._visited[x][y] != 0:
            return 0

        self._visited[x][y] = number
        count = 0
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if nx < 0 or nx >= self._n:
                continue
            if ny < 0 or ny >= self._n:
                continue
            count += self._fill_complex(nx, ny, number)

        return count + 1
        
    def numbering(self):
        num_complex = 0
        counts = []
        for i in range(self._n):
            for j in range(self._n):
                if self._m[i][j] == '1' and\
                   self._visited[i][j] == 0:
                    num_complex+=1
                    counts.append(
                        self._fill_complex(i, j, num_complex))

        return num_complex, counts
    

if __name__ == '__main__':
    n = int(stdin.readline())
    m = [list(stdin.readline()[:-1]) for _ in range(n)]

    nc = NumberingComplex(n, m)
    num_complex, counts = nc.numbering()
    print(num_complex)
    print('\n'.join(map(str, sorted(counts))))
    
