from sys import stdin


class Bulb():

    def __init__(self, n, status, goal):
        self.n = n
        self.status = status
        self.goal = goal

    def change_bulb(self, s, curr):
        if s < 0 or s >= self.n:
            return curr
        curr[s] = '0' if curr[s] == '1' else '1'
        return curr

    def push_button(self, x, curr):
        curr = self.change_bulb(x-1, curr)
        curr = self.change_bulb(x, curr)
        curr = self.change_bulb(x+1, curr)
        return curr

    def get_count(self, curr, g):
        count = 0
        for i in range(1, self.n):
            if curr[i-1] != g[i-1]:
                self.push_button(i, curr)
                count += 1
        if curr[-1] != g[-1]:
            return 0x7fffffff
        return count

    def get_min_count(self):
        # First bulb not pushed
        count_a = self.get_count(list(self.status), list(self.goal))

        curr = self.push_button(0, list(self.status))
        count_b = self.get_count(curr, list(self.goal)) + 1

        if count_a >= 0x7fffffff and count_b >= 0x7fffffff:
            return -1
        return min(count_a, count_b)


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    status = list(rd().strip())
    goal = list(rd().strip())
    bb = Bulb(n, status, goal)
    print(bb.get_min_count())
