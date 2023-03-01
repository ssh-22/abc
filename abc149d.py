"""
N回じゃんけんを行う
グーで勝った場合 -> R点
チェキで勝った場合 -> S点
パーで勝った場合 -> P点
K回前のじゃんけんと同じ手は出せない
K回目までのじゃんけんでは好きな手を出せる
相手が出す手は入力でわかっている(文字列T)
r -> グー
s -> チョキ
p -> パー
最大で合計何点得られるか

https://atcoder.jp/contests/abc149/tasks/abc149_d

貪欲
出す手をリストでメモする
K回目までのじゃんけん
    勝てる手を出す(R点 or S点 or P点)
K回目より後のじゃんけん
    1. 勝てる手がK回前と同じ手(0点)
    2. 勝てる手がK回前と違う手(R点 or S点 or P点)
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
ans = 0
winning = {"r": "p", "p": "s", "s": "r"}
winning_point = {"r": R, "s": S, "p": P}
rps = []
for i in range(N):
    idx = i + 1
    opponent_hand = T[i]
    if idx <= K:
        hand = winning[opponent_hand]
        rps.append(hand)
        ans += winning_point[hand]
    else:
        hand = winning[opponent_hand]
        before_k_hand = rps[i-K]
        if hand == before_k_hand:
            rps.append("x")
        else:
            rps.append(hand)
            ans += winning_point[hand]
print(ans)