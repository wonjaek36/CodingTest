from sys import stdin


class LCS(object):

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self._value = -1 

    def _get_lcs(self):
        lstr1 = len(self.str1)
        lstr2 = len(self.str2)
        table = [[0 for _ in range(lstr2+1)]
                 for _ in range(lstr1+1)]
        for i in range(1, lstr1+1):
            for j in range(1, lstr2+1):
                val = max(table[i-1][j], table[i][j-1])
                if self.str1[i-1] == self.str2[j-1]:
                    val = max(val, table[i-1][j-1]+1)
                table[i][j] = val
        self._value = table[lstr1][lstr2]

    @property
    def value(self):
        if self._value == -1:
            self._get_lcs()
        return self._value


if __name__ == '__main__':
    rd = stdin.readline
    str1 = rd().strip()
    str2 = rd().strip()
    lcs = LCS(str1, str2)
    print(lcs.value)

