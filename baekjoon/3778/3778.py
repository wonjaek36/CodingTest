import sys
from sys import stdin


class Anagram(object):

    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2

    def _get_character_count(self, s):
        alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
        return {k: s.count(k) for k in alphabets}
        
    def get_distance(self):
        d1 = sorted(self._get_character_count(self._s1).items())
        d2 = sorted(self._get_character_count(self._s2).items())
        distance = 0

        for a, b in zip(d1, d2):
            distance += abs(a[1]-b[1])
        return distance


if __name__ == '__main__':
    T = int(stdin.readline())

    for i in range(T):
        s1 = stdin.readline()[:-1]
        s2 = stdin.readline()[:-1]
    
        anagram = Anagram(s1, s2)
        print('Case #{}: {}'.format(
            i+1, anagram.get_distance()))
