from sys import stdin


class Permutation(object):

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._list = []
        self._visited = [False for _ in range(n)]

    def _permutate(self, c, p):
        if c >= self._m:
            self._list.append(p.copy())
            return

        s = 0 if len(p) == 0 else int(p[-1])
        for i in range(s, self._n):
            p.append(str(i+1))
            self._visited[i] = True
            self._permutate(c+1, p)
            self._visited[i] = False
            p.pop()

    def permutate(self):
        self._permutate(0, [])
        return self._list


if __name__ == '__main__':
    rd = stdin.readline
    n, m = list(map(int, rd().split(' ')))

    p = Permutation(n, m)
    p_list = p.permutate()
    print('\n'.join(map(lambda x: ' '.join(x), p_list)))
