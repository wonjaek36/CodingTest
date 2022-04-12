import sys
from sys import stdin
sys.setrecursionlimit(10**6)


class FormulaTree:

    def __init__(self, tree, nums):
        self._tree = tree
        self._root = self._find_root()
        self._nums = sorted(nums)
        self._lp = 0
        self._rp = len(self._nums)-1
        
    def _find_root(self):
        for k, v in self._tree.items():
            if v['p'] == -1:
                return k
        return -1

    def run_formula(self):
        return self._calculate(self._root, 0)

    def _calculate(self, n, lmc):
        if self._tree[n]['l'] == -1:
            return self._get_value(lmc)

        lv = self._calculate(self._tree[n]['l'], lmc)
        rv = self._calculate(
            self._tree[n]['r'],
            lmc+1 if self._tree[n]['op'] == '-' else lmc)
        
        if self._tree[n]['op'] == '-':
            return lv - rv
        else:
            return lv + rv
        
    def _get_value(self, lmc):
        if lmc % 2 == 0:
            self._rp -= 1
            return self._nums[self._rp+1]
        self._lp += 1
        return self._nums[self._lp-1]

    
if __name__ == '__main__':
    n = int(stdin.readline())
    numbers = []
    operators = []
    tree = {i: {'p': -1, 'l': -1, 'r': -1} for i in range(1, n*2)}
    for _ in range(n):
        numbers.append(int(stdin.readline()))
    for i in range(n+1, n*2):
        op, a, b = stdin.readline().rstrip().split(' ')
        a, b = int(a), int(b)
        operators.append((op, a, b))
        tree[i]['op'] = op
        tree[i]['l'] = a
        tree[i]['r'] = b
        tree[a]['p'] = i
        tree[b]['p'] = i
    
    ft = FormulaTree(tree, numbers)
    print(ft.run_formula())
