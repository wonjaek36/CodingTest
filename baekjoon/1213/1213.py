import sys
from sys import stdin


ab = stdin.readline().rstrip()
alpha = {chr(i): 0 for i in range(65, 65+26)} 
for x in ab:
    alpha[x] += 1

odd = False
front = ""
end = ""
middle = ""
for k, v in sorted(alpha.items()):
    if v % 2 == 1 and odd:
        print('I\'m Sorry Hansoo')
        sys.exit(0)
    elif v % 2 == 1:
        odd = True
        middle = k

    front = front + k * (v // 2)
    end = k * (v // 2) + end

print(front + middle + end)
