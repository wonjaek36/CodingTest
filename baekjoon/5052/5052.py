import sys
from sys import stdin


class PhoneBook(object):

    class Node(object):
        def __init__(self, ch, is_number):
            self.ch = ch
            self.is_number = is_number
            self.children = [None] * 10

    def __init__(self, n, numbers):
        self._n = n
        self._numbers = numbers
        self._root = self.Node('', False)
    
    def is_consistent(self):
        result = True
        for num in self._numbers:
            result = result and self._add_num_to_trie(num)

        return 'YES' if result else 'NO'

    def _add_num_to_trie(self, num):
        cur = self._root
        for ch in num[:-1]:
            assert cur != None
            n = ord(ch) - ord('0')
            if cur.children[n] is None:
                cur.children[n] = self.Node(ch, False)
            elif cur.children[n].is_number:
                return False
            cur = cur.children[n]

        assert cur != None
        ch = num[-1]
        n = ord(ch) - ord('0')
        if cur.children[n] is None:
            cur.children[n] = self.Node(ch, True)
        elif cur.children[n].is_number:
            return False
        return True


if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        numbers = [stdin.readline().rstrip()
                for _ in range(n)]
        numbers = sorted(numbers, key=lambda x: len(x))
        pb = PhoneBook(n, numbers)
        print(pb.is_consistent())

