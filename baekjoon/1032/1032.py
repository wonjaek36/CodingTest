import sys
from sys import stdin


class PatternRecognizer(object):

    def __init__(self, n, strs):
        self._n = n
        self._strs = strs

    def get_pattern(self):
        pattern = ''

        for chs in zip(*self._strs):
            if len(set(chs)) != 1:
                pattern += '?'
            else:
                pattern += chs[0]

        return pattern


if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    strs = [stdin.readline().rstrip() for _ in range(n)]

    pr = PatternRecognizer(n, strs)
    print(pr.get_pattern())
    
