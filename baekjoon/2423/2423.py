from sys import stdin
import heapq


class LightUp(object):

    def __init__(self, n, m, mp):
        self.mp = [['-' for _ in range(m+2)] for _ in range(n+2)]
        for i in range(n):
            for j in range(m):
                self.mp[i+1][j+1] = mp[i][j]

        self.n = n+2
        self.m = m+2
        self.visited = [[[False] * 2 for _ in range(self.m)]
                        for _ in range(self.n)]
        self.mp[0][0] = '\\'
        self.mp[self.n-1][self.m-1] = '\\'
         
    def _is_connected(self, a: tuple, b: tuple) -> bool:
        ax, ay, ass = a
        bx, by, bss = b

        # 정방향 대각선
        if ax - bx == ay - by:
            return ass == '\\' and bss == '\\'
        # 역방향 대각선
        if ax + ay == bx + by:
            return ass == '/' and bss == '/'
        # 상하좌우
        if abs(ax-bx) + abs(ay-by):
            return ass != bss

        return False

    def _flip_line(self, s) -> str:
        if s == '/':
            return '\\'
        return '/'

    def get_smallest_change_path(self):
        h = [(0, 0, 0, '\\')]

        while h:
            chgs, x, y, line = heapq.heappop(h)
            stat_num = 0 if line == '\\' else 1
            if x == self.n-1 and y == self.m-1:
                return chgs
            if self.visited[x][y][stat_num]:
                continue
            self.visited[x][y][stat_num] = True

            for dx, dy in [[-1, -1], [-1, 0], [-1, 1],
                           [0, -1], [0, 1],
                           [1, -1], [1, 0], [1, 1]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= self.n:
                    continue
                if ny < 0 or ny >= self.m:
                    continue
                if self.mp[nx][ny] == '-':
                    continue

                cur_state = (x, y, line)
                nxt_state = (nx, ny, self.mp[nx][ny])
                nstat_num = 0 if nxt_state[-1] == '\\' else 1
                # No changes
                    
                if not self.visited[nx][ny][nstat_num] and \
                        self._is_connected(cur_state, nxt_state):
                    heapq.heappush(h, (chgs, *nxt_state))

                # Changes
                nxt_state = (nx, ny, self._flip_line(self.mp[nx][ny]))
                nstat_num = 0 if nxt_state[-1] == '\\' else 1
                if not self.visited[nx][ny][nstat_num] and \
                    self._is_connected(cur_state, nxt_state):
                    heapq.heappush(h, (chgs+1, *nxt_state))

        return 'NO SOLUTION'

if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    mp = [list(rd().rstrip()) for _ in range(n)]
    lu = LightUp(n, m, mp)
    print(lu.get_smallest_change_path())
