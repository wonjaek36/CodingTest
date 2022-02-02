import sys
import math


class NoSquareNumber(object):

    def __init__(self, mn, mx):
        self._mn = mn
        self._mx = mx
        self._prime_set = set()

    def _find_prime_numbers(self):
        non_prime_set = set()
        l = int(self._mx**0.5 + 1)
        for num in range(2, l):
            if num in non_prime_set:
                continue
            self._prime_set.add(num)
            for k in range(num+num, l, num):
                non_prime_set.add(k)

    def _find_square_numbers(self):
        square_set = set()
        primes = list(self._prime_set)
        for p in primes:
            sq = p*p
            s_sq = self._mn//sq*sq
            if s_sq < self._mn:
                s_sq = s_sq + sq
            for k in range(s_sq, self._mx+1, sq):
                square_set.add(k)

        return len(square_set)

    def get_number_of_non_squares(self):
        self._find_prime_numbers()
        num_of_square_num = self._find_square_numbers()
        return self._mx - self._mn + 1 - num_of_square_num


if __name__ == '__main__':
    mn, mx = list(map(int, sys.stdin.readline().split(' ')))
    nsn = NoSquareNumber(mn, mx)
    print(nsn.get_number_of_non_squares())
    
