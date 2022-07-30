from sys import stdin


class PuyoPyuo(object):

    def __init__(self, arr):
        self.arr = arr
        self.visited = None

    def _find_same_color(self, x, y, c, k):
        if x < 0 or x >= 12:
            return 0
        if y < 0 or y >= 6:
            return 0
        if self.arr[x][y] != c:
            return 0
        if self.visited[x][y] != 0:
            return 0

        assert self.visited is not None 
        self.visited[x][y] = k
        count = self._find_same_color(x+1, y, c, k) +\
            self._find_same_color(x, y+1, c, k) +\
            self._find_same_color(x-1, y, c, k) +\
            self._find_same_color(x, y-1, c, k)
        return count + 1

    def boom_checker(self):
        self.visited = [[False]*6 for _ in range(12)]
        boom_list = []
        k = 0
        cnt = 0
        for i in range(12):
            for j in range(6):
                if self.arr[i][j] != '.':
                    k += 1
                    cnt = self._find_same_color(
                        i, j, self.arr[i][j], k)
                    if cnt >= 4:
                        boom_list.append(k)
        return boom_list

    def boom(self, boom_list):
        assert self.visited is not None 
        for i in range(12):
            for j in range(6):
                if self.visited[i][j] in boom_list:
                    self.arr[i][j] = '.'
        
        for i in range(6):
            for j in range(11, -1, -1):
                if self.arr[j][i] != '.':
                    continue
                for k in range(j-1, -1, -1):
                    if self.arr[k][i] != '.':
                        self.arr[j][i] = self.arr[k][i]
                        self.arr[k][i] = '.'
                        break

    def get_boom_count(self):
        count = 0
        while True:
            boom_list = self.boom_checker()
            if len(boom_list) == 0:
                break
            self.boom(boom_list)
            # self._print()
            count += 1
        return count


if __name__ == '__main__':
    rd = stdin.readline
    arr = [list(rd().strip()) for _ in range(12)]
    pp = PuyoPyuo(arr)
    print(pp.get_boom_count())
