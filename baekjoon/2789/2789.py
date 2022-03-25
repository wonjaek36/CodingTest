import sys

a = sys.stdin.readline().rstrip()
print(''.join(list(filter(lambda x: x not in 'CAMBRIDGE', a))))
