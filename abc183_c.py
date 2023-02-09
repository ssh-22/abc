
"""
概要
都市1を出発し、すべての都市を1度訪問してから都市1に戻る経路を列挙する
移動時間の合計がKになるものがいくつあるか

解法
すべての経路を列挙し、移動時間の合計を計算する
合計がKになる数をカウントする

URL
https://atcoder.jp/contests/abc183/tasks/abc183_c

入力
4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0

出力
2

"""
import itertools
N, K = map(int, input().split())
combs = list(itertools.permutations(range(1, N), N-1))
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for comb in combs:
    comb += (0,)
    travel_time = 0
    prev_city = 0
    for next_city in comb:
        travel_time += T[prev_city][next_city]
        prev_city = next_city
    if travel_time == K:
        ans += 1
print(ans)
