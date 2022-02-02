import sys
from collections import deque


class DFS(object):
	
	def __init__(self, n, v, edges):
		self._n = n
		self._v = v
		self._edges = edges
		self._stack = []
		self._visited = [False] * (n+1)

	def _push(self, node):
		self._stack.append(node)

	def _pop(self):
		return self._stack.pop()

	def search(self):
		traverse = []
		self._push(self._v)
		while len(self._stack) != 0:
			c = self._pop()
			if self._visited[c]:
				continue
			self._visited[c] = True
			traverse.append(c)

			for nxt in sorted(self._edges[c])[::-1]:
				if self._visited[nxt]:
					continue
				self._push(nxt)

		return traverse


class BFS(object):
	
	def __init__(self, n, v, edges):
		self._n = n
		self._v = v
		self._edges = edges
		self._queue = deque([])
		self._visited = [False] * (n+1)

	def _push(self, node):
		self._queue.append(node)

	def _pop(self):
		return self._queue.popleft()

	def search(self):
		traverse = []
		self._push(self._v)
		while len(self._queue) != 0:
			c = self._pop()
			if self._visited[c]:
				continue
			self._visited[c] = True
			traverse.append(c)

			for nxt in sorted(self._edges[c]):
				if self._visited[nxt]:
					continue
				self._push(nxt)

		return traverse


if __name__ == '__main__':
	n, m, v = list(map(int, sys.stdin.readline().split(' ')))
	edges = {}
	for i in range(1, n+1):
		edges[i] = set()

	for _ in range(m):
		s, e = list(map(int, sys.stdin.readline().split(' ')))
		edges[s].add(e)
		edges[e].add(s)

	dfs = DFS(n, v, edges)
	print(' '.join(map(str, dfs.search())))
	bfs = BFS(n, v, edges)
	print(' '.join(map(str, bfs.search())))
