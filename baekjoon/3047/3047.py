import sys

items = list(map(lambda x: int(x), sys.stdin.readline().split(' ')))
seq = list(map(lambda x: ord(x)-65, list(sys.stdin.readline())[:-1]))
items = list(map(lambda x: str(x), sorted(items)))
items = [items[i] for i in seq]
print(' '.join(items))
