from sys import stdin


_, k = map(int, stdin.readline().split(' '))
print(sorted(map(int, stdin.readline().split(' ')))[k-1])
