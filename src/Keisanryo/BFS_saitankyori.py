from collections import deque

graph = {
    0: [1,2],
    1: [3],
    2: [3],
    3: []
}

def bfs(start):
    dist = [-1]*4
    dist[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist

print(bfs(0))