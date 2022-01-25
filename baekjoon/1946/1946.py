import sys


class Recruiter(object):

    def __init__(self, ranks):
        self.ranks = ranks

    def hire(self):
        ranks = sorted(self.ranks, key=lambda x: x[0])
        inter_high = ranks[0][1]
        count = 1
        for _, interview in ranks[1:]:
            if interview < inter_high:
                inter_high = interview
                count += 1

        return count

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        ranks = []
        for _ in range(N):
            employee_rank = list(
                map(lambda x: int(x), sys.stdin.readline().split(' ')))
            ranks.append(employee_rank)

            recuriter = Recruiter(ranks)
        print(recuriter.hire())
            
        
