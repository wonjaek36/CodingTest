import sys
import time


class Sudoku(object):

    def __init__(self, su_map):
        self.su_map = su_map
        self.blanks = []
        self.row_pos = None
        self.ver_pos = None
        self.squ_pos = None
        self.len_blanks = 0

    def _find_blanks(self):
        for i in range(9):
            for j in range(9):
                if self.su_map[i][j] == 0:
                    self.blanks.append((i, j))
        self.len_blanks = len(self.blanks)

    def _get_possibles(self):
        self.row_pos = [[False]*9 for _ in range(9)]
        self.ver_pos = [[False]*9 for _ in range(9)]
        self.squ_pos = [[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if self.su_map[i][j] != 0:
                    self.row_pos[i][self.su_map[i][j]-1] = True
                    squ_num = i//3*3+j//3
                    self.squ_pos[squ_num][self.su_map[i][j]-1] = True
                    self.ver_pos[j][self.su_map[i][j]-1] = True

    def _fill_map(self, pos):
        if self.len_blanks == pos:
            return True
        
        x, y = self.blanks[pos]
        squ_num = x//3*3+y//3
        for i in range(1, 10):
            if self.row_pos[x][i-1] or \
               self.ver_pos[y][i-1]  or \
               self.squ_pos[squ_num][i-1]:
                continue

            self.su_map[x][y] = i
            self.squ_pos[squ_num][i-1] = self.row_pos[x][i-1] = self.ver_pos[y][i-1] = True
            is_filled = self._fill_map(pos+1)
            if is_filled:
                return True
            self.su_map[x][y] = 0
            self.row_pos[x][i-1] = self.ver_pos[y][i-1] = self.squ_pos[squ_num][i-1] = False

        return False
    
    def solve(self):
        self._find_blanks()
        self._get_possibles()
        self._fill_map(0)

    def prnt(self):
        for row in self.su_map:
            print(' '.join(map(str, row)))


if __name__ == '__main__':
    sudoku_map = [
        [int(x) for x in sys.stdin.readline().split(' ')]
        for _ in range(9)]
    # start_time = time.time()
    sudoku_problem = Sudoku(sudoku_map)
    sudoku_problem.solve()
    sudoku_problem.prnt()
    # end_time = time.time()
    # print(end_time-start_time)
    
