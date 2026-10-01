# DFS　深さ優先探索
"""
[使用用途]
全頂点を訪問する
迷路を探索する
グラフが連結しているか調べる
木構造を探索する
バックトラックする
サイクルを検出する

# 発展として距離を記録するDFSもある
def dfs(v, dist):
    for nv in graph[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            dfs(nv, dist)
一般的な「重みなしグラフの最短距離」を求めるならBFSを使う
"""


graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

def dfs(v, visited):
    # v:探索開始場所　visited:頂点を訪れたかあらわすリスト 要素はtype:boolean
    visited[v] = True

    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv, visited)

# この頂点を訪れたかを表すリスト
visited = [False] * 4

dfs(0, visited)

print(visited)