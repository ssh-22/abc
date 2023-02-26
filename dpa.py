"""
N個の足場(1<=i<=N)がある
足場iの高さはhi
足場1にカエルがいる
足場iにいるとき、足場i+1またはi+2(j)にジャンプする
コストabs(hi-hj)を払う
Nに辿り着くまでに支払うコストの総和の最小値を求める

https://atcoder.jp/contests/dp/tasks/dp_a

DP問題
表を作る
dp[i]=足場iに辿り着くまでの最小コスト
i|1|2|3|4
h|10|30|40|20|
dp|0|20|30|30|
dp[0] = 0
dp[1] = 0
dp[i]は以下の最小値
1. 足場i-2から2つ飛ぶ
    dp[i-2] + |h(i-2)-h(i)|
2. 足場i-1から1つ飛ぶ
    dp[i-1] + |h(i-1)-h(i)|
"""
N = int(input())
h = [0] + list(map(int, input().split()))
INF = float("inf")
dp = [INF]* (N+1)
dp[1] = 0
for i in range(2, N+1):
    stone1 = dp[i-1] + abs(h[i-1]-h[i])
    stone2 = dp[i-2] + abs(h[i-2]-h[i])
    dp[i] = min(stone1, stone2)
print(dp[N])
