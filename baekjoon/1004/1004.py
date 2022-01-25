import sys
import math


class LittlePrincess(object):

    def __init__(self, travel, galaxies):
        self._travel = travel
        self._galaxies = galaxies

    def _get_distance(self, x1, y1, x2, y2):
        x = (x1-x2)*(x1-x2)
        y = (y1-y2)*(y1-y2)
        return math.sqrt(x+y)
        
    def _is_point_in_circle(self, x, y, circle):
        cx, cy, cn = circle
        distance = self._get_distance(x, y, cx, cy)
        return distance < cn
    
    def count_entry_galaxies(self):
        start_x, start_y, end_x, end_y = travel
        count = 0
        for galaxy in self._galaxies:
            start_in = self._is_point_in_circle(start_x, start_y, galaxy)
            end_in = self._is_point_in_circle(end_x, end_y, galaxy)

            if (start_in and not end_in) or (not start_in and end_in):
                count += 1
        return count

            
if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        travel = list(map(int, sys.stdin.readline().split(' ')))
        
        N = int(sys.stdin.readline())
        galaxies = []
        for _ in range(N):
            cx, cy, cn = map(int, sys.stdin.readline().split(' '))
            galaxies.append((cx, cy, cn))
        
        lp = LittlePrincess(travel, galaxies)
        print(lp.count_entry_galaxies())
