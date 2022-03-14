import sys
from sys import stdin

nums = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

N = int(stdin.readline())
for _ in range(N):
    a, b = list(
        map(int,
            stdin.readline().rstrip().split(' ')))
    a = a%10
    b = b % len(nums[a])
    print(nums[a][b-1])
