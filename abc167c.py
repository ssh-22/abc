"""
学びたいアルゴリズムがM個ある
各アルゴリズムの理解度の初期値は0
N冊の参考書が売っている
i番目の参考書(1<=i<=N)はCi円で売られている
j番目のアルゴリズム(1<=j<=M)の理解度がAij上がる
目標はM個全てのアルゴリズムの理解度をX以上にすること
目標が達成できるなら必要な金額の最小値を出力する
できないなら-1を出力する
1<=N,M<=12

https://atcoder.jp/contests/abc167/tasks/abc167_c

1. bit全探索で各参考書について、買うか買わないか全て試す
2. 買う場合、各参考書の値段を加算する
3. 各参考書の値段の最小値がX以上だったらansを更新する
4. ansが更新されていたらansを出力する、されていなかったら-1を出力する
"""
N, M, X = map(int, input().split())
INF = float("inf")
ans = INF
C = []
A = []
for i in range(N):
    AC = list(map(int, input().split()))
    C.append(AC[0])
    A.append(AC[1:])
# 1をNだけ左シフト(2のN乗)
for i in range(1 << N):
    # 購入した参考書の値段の合計
    cost = 0
    # M個の各アルゴリズムの理解度
    skill = [0]*M
    # iをjだけ右シフト(2, 100->001)して、1とAND演算(001&1)
    for s in range(N):
        if i >> s & 1:
            cost += C[s]
            for j in range(M):
                skill[j] += A[s][j]
    if min(skill) >= X:
        ans = min(ans, cost)
if ans == INF:
    print(-1)
else:
    print(ans)