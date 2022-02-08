from sys import stdin


class ShootingStar(object):

    def __init__(self, r, s, pic):
        self._r = r
        self._s = s
        self._pic = pic
        self._recovered = [['.']*self._s for _ in range(self._r)] 

    def _get_column_fall_length(self, col):
        bot_star = -1
        top_ground = self._r-1
        
        for i in range(self._r):
            if self._pic[self._r-i-1][col] == 'X':
                bot_star = self._r-i-1
                break

        for i in range(self._r):
            if self._pic[i][col] == '#':
                top_ground = i
                break

        fall_length = top_ground-bot_star-1
        if bot_star == -1:
            fall_length = self._r
        return fall_length
        
    def _get_star_fall_length(self):
        fall_length = self._r+1
        for i in range(self._s):
            fall_length = min(fall_length,
                              self._get_column_fall_length(i))
        return fall_length
        
    def recover(self):
        fall_length = self._get_star_fall_length()

        for i in range(self._r):
            for j in range(self._s):
                if self._pic[i][j] == 'X':
                    self._recovered[i+fall_length][j] = 'X'
                if self._pic[i][j] == '#':
                    self._recovered[i][j] = '#'

        return self._recovered


if __name__ == '__main__':
    r, s = list(map(int, stdin.readline().split(' ')))
    pic = [list(stdin.readline())[:-1] for _ in range(r)]

    ss = ShootingStar(r, s, pic)
    recovered = ss.recover()
    for i in range(len(recovered)):
        print(''.join(recovered[i]))
