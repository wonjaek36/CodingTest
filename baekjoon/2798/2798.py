import sys


class BlackJack(object):

    def __init__(self, M, cards):
        self._M = M
        self._cards = cards
        self._best = 1e10

    def _return_best_cards(self, a, b):
        if self._M-a > self._M-b:
            return b
        else:
            return a
        
    def _search_cards_sum(self, p, c, s):
        if s > self._M:
            return 0
        if c == 3:
            return s
        elif p == len(self._cards):
            return 0

        a = self._search_cards_sum(p+1, c, s)
        b = self._search_cards_sum(
            p+1, c+1, s+self._cards[p])
        return self._return_best_cards(a, b)
        
    def find_best_card_sum(self):
        return self._search_cards_sum(0, 0, 0)
                    

if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split(' ')))
    cards = list(map(int, sys.stdin.readline().split(' ')))

    blackjack = BlackJack(M, cards)
    print(blackjack.find_best_card_sum())

                
