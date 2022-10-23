from sys import stdin
import heapq
inf = 0x7fffffff

def fox_dijkstra(graph):
    h = [(0, 0)]
    fox = [inf for _ in range(n)]

    while h:
        d, p = heapq.heappop(h)
        if fox[p] < d:
            continue

        for nxt, nxt_dis in graph[p]:
            if fox[nxt] > d + nxt_dis:
                fox[nxt] = d + nxt_dis
                heapq.heappush(h, (d+nxt_dis, nxt))
    return fox


def wolf_dijkstra(graph):
    h = [(0, 0, 0)] # distance, status, location
    wolf = [[inf for _ in range(n)] for _ in range(2)]

    while h:
        d, s, p = heapq.heappop(h)
        if wolf[s][p] < d:
            continue

        ns = 1 if s == 0 else 0
        for nxt, nxt_dis in graph[p]:
            nd = d + (nxt_dis//2 if s == 0 else nxt_dis*2)
            if wolf[ns][nxt] > nd:
                wolf[ns][nxt] = nd
                heapq.heappush(h, (nd, ns, nxt))

    return wolf


rd = stdin.readline
n, m = tuple(map(int, rd().split()))
edges = []
for _ in range(m):
    a, b, d = tuple(map(int, rd().split()))
    edges.append((a-1, b-1, d*2))

graph = {i: [] for i in range(n)}
for a, b, d in edges:
    graph[a].append((b, d))
    graph[b].append((a, d))

fox = fox_dijkstra(graph)
wolf = wolf_dijkstra(graph)

count = 0
for wa, wb, f  in zip(wolf[0], wolf[1], fox):
    if f < min(wa, wb):
        count += 1
print(count)
