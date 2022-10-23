from sys import stdin


class TeamSplit(object):

    def __init__(self, n, mp):
        self.n = n
        self.nums = list(range(n))
        self.mp = mp
        self.members = [False for _ in range(self.n)]
        self.min_val = 0x7fffffff
        self.flag = False
    
    def get_score(self, team_member):
        score = 0
        for idx, (i, _) in enumerate(team_member):
            for j, _ in team_member[idx:]:
                score += (self.mp[i][j] + self.mp[j][i])
        return score

    def get_differences_score(self):
        teamA = list(
            filter(lambda x: not x[1], enumerate(self.members)))
        teamB = list(
            filter(lambda x: x[1], enumerate(self.members)))
        scoreA, scoreB = self.get_score(teamA), self.get_score(teamB)
        return abs(scoreA - scoreB)

    def select_team(self, i, pos):
        if pos == self.n // 2:
            diff = self.get_differences_score()
            self.min_val = min(diff, self.min_val)
            return

        if i >= self.n:
            return

        for k in self.nums[i:]:
            self.members[k] = True
            self.select_team(k+1, pos+1)
            self.members[k] = False

    def split(self):
        self.select_team(0, 0)
        return self.min_val


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    mp = [
        list(map(int, rd().split())) for _ in range(n)]
    ts = TeamSplit(n, mp)
    print(ts.split())
