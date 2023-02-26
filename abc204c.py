"""
N個の都市とM個の道路がある
道路iを通るとAiからBiへ移動できる
BiからAiへの通行はできない
どこかの都市からスタートし、0本以上の道路を使い移動して、どこかの都市をゴールとする旅行の計画を立てる
スタート地点とゴール地点の都市の組として考えられるものは何通りあるか

https://atcoder.jp/contests/abc204/tasks/abc204_c

幅優先探索(BFS)を使う
スタート地点の都市を固定して、到達できる都市(ゴール)の数を合計する
1. 1からMの都市について以下の処理を実行する
    1. スタート地点に訪問済みマークをつける
    2. スタート地点をゴールとしてカウントを+1する
    3. スタート地点をqueに入れる
    4. queの要素がなくなるまで以下の操作を繰り返す
        1. queの左端から要素を取り出す
        2. 取り出した都市から行ける都市を取得する
        3. 訪問済みマークがついていないものにマークをつける
        4. ゴールとしてカウントを+1する
        5. マークをつけた都市をqueに入れる
2. カウントを出力する
"""
from collections import deque

def bfs(start: int, connect: list[int]) -> int:
    count = 0
    visited = [False] * (N+1)
    # スタート地点に訪問済みマークをつける
    visited[start] = True
    # スタート地点をゴールとしてカウントを+1する
    count += 1
    # スタート地点をqueに入れる
    que = deque([start])
    # queの要素がなくなるまで以下の操作を繰り返す
    while que:
        # queの左端から要素を取り出す
        from_city = que.popleft()
        # 取り出した都市から行ける都市を取得する
        for to_city in connect[from_city]:
            # 訪問済みマークがついていないものにマークをつける
            if visited[to_city] is False:
                visited[to_city] = True
                count += 1
                que.append(to_city)
    return count

N, M = map(int, input().split())
connect = [[] for _ in range(N+1)]
ans = 0
for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
for i in range(1, N+1):
    ans += bfs(i, connect)
print(ans)
