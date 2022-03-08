import sys
from sys import stdin


N = int(stdin.readline().rstrip())
print('\n'.join(
    map(str, sorted([int(stdin.readline().rstrip()) for _ in range(N)]))))



