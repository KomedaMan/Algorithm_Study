from collections import deque

# グラフを作る　例えば0は1, 2に進むことができる
# 1は3、2も3に進むことができる
# 3はどこにも行けないので終点である
# 辞書型で表す
graph = {
    0: [1,2],
    1: [3],
    2: [3],
    3: []
}


def bfs(start):  # start:どの頂点から探索を始めるか
    # distはスタート地点から各頂点までの距離
    # 要素が4つなのでありえない値を設定してそれを4要素作成する（-1はまだ訪れていないことを表す）
    dist = [-1]*4
    dist[start] = 0     # スタート地点の距離は0
    # これから調べる頂点を入れるキューを作成する
    q = deque([start])      # 初期値はスタート地点のみ調べるのでstartを入れておく

    # キューが空になるまで繰り返す
    while q:
        v = q.popleft()     # 先頭要素を一つとりだす
        # 現在調べている頂点vから直接行ける頂点を1つずつ調べる
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist

print(bfs(0))