from sys import stdin


class PlumTree(object):

    def __init__(self, t, w, falls):
        self.t = t
        self.w = w
        self.falls = falls
        self.dp = []

    def swap_location(self, location):
        if location == 0:
            return 1
        else:
            return 0

    def get_better_prev(self, time, remain_step, location, fall):
        val = self.dp[time][remain_step][location] + \
            (1 if location == fall else 0)
        if remain_step + 1 <= self.w and time != 1:
            val = max(
                val,
                self.dp[time][remain_step+1][self.swap_location(location)] +\
                1 if location == fall else 0)
        return val

    def get_max(self):
        self.dp.append([[0, 0] for _ in range(self.w+1)])
        for t, fall in enumerate(self.falls):
            self.dp.append([[0, 0] for _ in range(self.w+1)])
            for _w in range(self.w+1):
                self.dp[t+1][_w][0] = self.get_better_prev(t, _w, 0, fall)
                self.dp[t+1][_w][1] = self.get_better_prev(t, _w, 1, fall)

        return max(map(max, self.dp[self.t]))

if __name__ == '__main__':
    rd = stdin.readline
    t, w = list(map(int, rd().split(' ')))
    falls = [int(rd())-1 for _ in range(t)]

    pt = PlumTree(t, w, falls)
    print(pt.get_max())
