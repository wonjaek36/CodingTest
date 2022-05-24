from sys import stdin


class Permutation(object):

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._list = []
        self._used = [False for _ in range(n)]

    def _permutate(self, c, p):
        if self._m <= c:
            self._list.append(p.copy())
            return

        for i in range(self._n):
            if self._used[i]:
                continue

            p.append(str(i+1))
            self._used[i] = True
            self._permutate(c+1, p)
            self._used[i] = False 
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
