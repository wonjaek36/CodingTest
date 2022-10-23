from sys import stdin


class Sale(object):

    def __init__(self, milks):
        self.milks = sorted(milks, reverse=True)

    def get_cheapest(self):
        price = 0
        for i in range(0, len(self.milks), 3):
            try:
                price += (self.milks[i] + self.milks[i+1])
            except IndexError:
                price += self.milks[i]

        return price


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    milks = [int(rd()) for _ in range(n)]

    s = Sale(milks)
    print(s.get_cheapest())
