from sys import stdin


class Resturant(object):

    def __init__(self, n, foods: list):
        self.n = n
        self.foods = foods
        self.foods = sorted(self.foods, key=lambda x: x[1])

    def _create_min_last_fo(self):
        min_fo = [0] * self.n
        min_fo[0] = self.foods[-1][0]
        for idx, food in enumerate(reversed(self.foods[:-1])):
           min_fo[idx+1] = min(min_fo[idx], food[0])
        return list(reversed(min_fo))

    @property
    def prices(self) -> list:
        min_fo = self._create_min_last_fo()
        min_diff = 0x7fffffff

        price = 0
        best_prices = []
        for idx, (a, b) in enumerate(self.foods):
            min_diff = min(min_diff, a-b)
            best_prices.append(min(price+min_diff+b, price+min_fo[idx]))
            price += b

        return best_prices


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    foods = [tuple(map(int, rd().split(' ')))
             for _ in range(n)]

    rs = Resturant(n, foods)
    prices = rs.prices
    print(*prices, sep='\n')


