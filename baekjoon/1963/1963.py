from sys import stdin
from collections import deque


class PrimePath(object):

    @classmethod
    def get_is_primes(cls):
        try:
            is_primes = getattr(cls, 'is_primes')
            return is_primes
        except AttributeError:
            pass
        
        cls.is_primes = [True for _ in range(10000)]
        for i in range(2, 10000):
            if not cls.is_primes[i]:
                continue
            for j in range(i+i, 10000, i):
                cls.is_primes[j] = False
        return cls.is_primes

    def __init__(self, frm, to):
        self.frm = frm
        self.to = to

    def changed_list(self, n):
        num, count = n
        changes = []
        for i in range(4):
            for j in range(10):
                target = list(str(num))
                target[i] = str(j)
                target = int(''.join(target))
                changes.append((target, count+1))

        changes = list(filter(lambda x: x[0] >= 1000, changes))
        return changes

    def get_path_count(self):
        is_primes = self.get_is_primes()
        dq = deque([(self.frm, 0)])
        visited = [False for _ in range(10000)]
        while len(dq) != 0:
            n = dq.popleft()

            visited[n[0]] = True
            if n[0] == self.to:
                return n[1]

            changes = self.changed_list(n)
            changes = list(filter(lambda x: is_primes[x[0]], changes))
            changes = list(filter(lambda x: not visited[x[0]], changes))
            for num, _ in changes:
                visited[num] = True

            dq.extend(changes)

        return 'Impossible'


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    for i in range(n):
        a, b = list(map(int, rd().split()))
        pp = PrimePath(a, b)
        print(pp.get_path_count())
