from sys import stdin

s = 0
for i in range(8):
    l = stdin.readline()[:-1]
    s += list(l[i%2::2]).count('F')

print(s)
