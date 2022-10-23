from sys import stdin


class Alphametic(object):

    def __init__(self, items):
        self.items = items
        self.length = max(
            list(map(lambda x: len(x), items)))
        chars = set()
        for item in items:
            chars.update(set(list(item)))
        chars = list(chars)
        self.chars = {ch: -1 for ch in chars}
        self.is_used = [False for _ in range(10)]
        self.chars[' '] = 0
        self._is_possible = False

    def _get_chars(self, col, row):
        try:
            return self.items[row][-col]
        except Exception:
            return ' '
    def _recur(self, col, row, carry):
        if col > self.length and carry == 0:
            fc = self.items[2][0]
            return True

        rt = False
        if row == 2:
            fc, sc = self._get_chars(col, 0), self._get_chars(col, 1)
            v1, v2 = self.chars[fc], self.chars[sc]
            rc = self._get_chars(col, 2)
            r = v1 + v2 + carry

            if self.chars[rc] == -1 and not self.is_used[r%10]:
                self.chars[rc] = r%10
                self.is_used[r%10] = True
                rt = self._recur(col+1, 0, r//10)
                self.chars[rc] = -1
                self.is_used[r%10] = False
            elif self.chars[rc] == r%10:
                rt = self._recur(col+1, 0, r//10)
        
        else:
            c = self._get_chars(col, row)
            if self.chars[c] == -1:
                for i in range(10):
                    if self.is_used[i]:
                        continue

                    self.chars[c] = i
                    self.is_used[i] = True
                    rt = self._recur(col, row+1, carry)
                    if rt:
                        break
                    self.chars[c] = -1
                    self.is_used[i] = False
            else:
                rt = self._recur(col, row+1, carry)
        return rt

    def is_possible(self):
        return 'YES' if self._recur(1, 0, 0) else 'NO'


if __name__ == '__main__':
    items = stdin.readline().strip()
    items = items.split(' ')
    
    a = Alphametic(items)
    print(a.is_possible())

