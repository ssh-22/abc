"""
概要
ロボットが階段のちょうどX段目に登ることができるか求める

解法
今いる段数をdp配列でもつ
モチが設置されている段をでcan_move配列でもつ
dp[i] = i段目に登ることができるならTrue、できないならFalse
dp[0] = True
dp[i]
    1. if not can_move[i]
        dp[i] = False
    2. else:
        dp[i] = dp[i-Aj]
i-Ajのいずれかの段に登れるならi番目に登れる
6段目(dp[i])に登れる
    1. 6段目(Aj=3)
        dp[6] |= dp[6-3]
    2. 6段目(Aj=4)
        dp[6] |= dp[6-4]
    3. 6段目(Aj=5)
        dp[6] |= dp[6-5]

URL
https://atcoder.jp/contests/abc199/tasks/abc199_c
"""
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())
dp = [False] * (X+1)
can_move = [True] * (X+1)
dp[0] = True
for b in B:
    can_move[b] = False
for i in range(1, X+1):
    # 1, 2, 3, ..., 15
    if not can_move[i]:
        dp[i] = False
    else:
        for a in A:
            # 3, 4, 5
            if i >= a:
                # i=3, a=3, i-a=0
                # i=4, a=3, i-a=1
                # .
                # .
                # .
                # i=15, a=3, i-a=12
                # i=4, a=4, i-a=0
                # i=5, a=5, i-a=1
                # .
                # .
                dp[i] |= dp[i-a]
if dp[X]:
    print("Yes")
else:
    print("No")
