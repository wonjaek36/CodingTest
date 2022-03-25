import sys
from functools import reduce

a = sys.stdin.readline()
parens = a.split('-')
s = reduce(lambda x, y: x+y, list(map(int, parens[0].split('+'))), 0)

for paren in parens[1:]:
    s = s - reduce(lambda x, y: x+y, list(
        map(int, paren.split('+'))), 0)

print(s)
    
