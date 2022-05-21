from sys import stdin


class ColoringHouse(object):

    def __init__(self, costs):
        self.costs = costs
        self.n = len(costs)
        self.dp = []

    def init_dp(self):
        self.dp.append(tuple(self.costs[0]))

    def min_cost_color(self, i):
        return (min(self.dp[i-1][1], self.dp[i-1][2]) + self.costs[i][0],
                min(self.dp[i-1][0], self.dp[i-1][2]) + self.costs[i][1],
                min(self.dp[i-1][0], self.dp[i-1][1]) + self.costs[i][2])

    def coloring(self):
        self.init_dp()
        for i in range(1, self.n):
            self.dp.append(self.min_cost_color(i))

        return min(self.dp[-1])


if __name__ == '__main__':
    rd = stdin.readline
    T = int(rd())
    costs = []
    for _ in range(T):
        r, g, b = list(map(int, rd().split(' ')))
        costs.append((r, g, b))

    ch = ColoringHouse(costs)
    print(ch.coloring())


