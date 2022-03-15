import sys
from sys import stdin


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


n, m = list(map(
    int, stdin.readline().rstrip().split(' ')))
_gcd = gcd(n, m)
print(_gcd)
print(int(n*m/_gcd))
