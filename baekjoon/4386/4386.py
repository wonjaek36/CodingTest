import sys
from sys import stdin
import heapq
import math


class Constellation(object):

	def __init__(self, stars):
		self._stars = stars
		self._visited = [False for _ in stars]
		self._heap = []

	def get_distance(self, s1, s2):
		return math.sqrt(math.pow(s1[0]-s2[0], 2) + math.pow(s1[1]-s2[1], 2))

	def get_weight(self):
		heapq.heappush(self._heap, (0, 0))
		connected = 0
		weight = 0
		while connected < n:
			d, cur = heapq.heappop(self._heap)
			if self._visited[cur]:
				continue

			weight += d
			connected += 1
			self._visited[cur] = True
			for idx, (nxt, v) in enumerate(zip(self._stars, self._visited)):
				if v:
					continue

				dis = self.get_distance(self._stars[cur], nxt)	
				heapq.heappush(self._heap, (dis, idx))
		return weight


if __name__ == '__main__':

	n = int(stdin.readline())
	stars = []
	for _ in range(n):
		a, b = list(map(float, stdin.readline().rstrip().split(' ')))
		stars.append((a, b))

	ct = Constellation(stars)
	print(f'{ct.get_weight():.2f}')
