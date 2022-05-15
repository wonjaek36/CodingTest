import sys
from sys import stdin
sys.setrecursionlimit(10**6)
INT_MAX = 0x7fffffff


class Histogram(object):

    def __init__(self, hist):
        self._hist = hist
        self._t = [0] * (len(hist)*4)
        self._construct_tree(1, 0, len(hist)-1)

    def _construct_tree(self, tree_node, left, right):
        if left == right:
            self._t[tree_node] = (self._hist[left], left)
            return (self._hist[left], left)

        mid = (left+right) // 2
        left_part = self._construct_tree(tree_node*2, left, mid)
        right_part = self._construct_tree(tree_node*2+1, mid+1, right)

        self._t[tree_node] = min(left_part, right_part)
        return self._t[tree_node]

    def _query(self, left, right,
               tree_node,
               tree_left, tree_right):

        if right < tree_left or tree_right < left:
            return (INT_MAX, INT_MAX)
        if left <= tree_left and tree_right <= right:
            return self._t[tree_node]

        tree_mid = (tree_left + tree_right) // 2
        left_part = self._query(
            left, right, tree_node*2, tree_left, tree_mid)
        right_part = self._query(
            left, right, tree_node*2+1, tree_mid+1, tree_right)

        return min(left_part, right_part)

    def query(self, left, right):
        val = self._query(left, right, 1, 0, len(self._hist)-1)
        assert type(val) is tuple
        return val

    def _get_max_area(self, left, right):
        if right < left or left < 0 or right >= len(self._hist):
            return 0
        if left == right:
            return self.query(left, right)[0]

        height, idx = self.query(left, right)
        area = (right-left+1)*height
        left_area = self._get_max_area(left, idx-1)
        right_area = self._get_max_area(idx+1, right)

        return max(area, left_area, right_area)

    def get_max_area(self):
        return self._get_max_area(0, len(self._hist)-1)


if __name__ == '__main__':
    rd = stdin.readline

    arr = []
    n = int(rd())
    for _ in range(n):
        arr.append(int(rd()))
    h = Histogram(arr)
    print(h.get_max_area())
