"""
小文字からなる文字列S
Q回(1<=i<=Q)の操作を行う
1. 整数Tiが1:
    文字列Sの前後を反転する
2. 整数Tiが2:
    追加で整数Fiと英小文字Ciが与えられる
    1. Fiが1
        Sの先頭にCiを追加する
    2. Fiが2
        Sの末尾にCiを追加する
最終的にできる文字列を出力する

https://atcoder.jp/contests/abc158/tasks/abc158_d

dequeを利用する
1. 整数Tiが1:
    文字列Sの前後を反転する
    flip = not flip
2. 整数Tiが2:
    追加で整数Fiと英小文字Ciが与えられる
    1. Fiが1
        Sの先頭にCiを追加する
        1. flipがFalse -> Sの先頭にCiを追加する
        2. flipがTrue -> Sの末尾にCiを追加する
    2. Fiが2
        Sの末尾にCiを追加する
        1. flipがFalse -> Sの末尾にCiを追加する
        2. flipがTrue -> Sの先頭にCiを追加する
"""
from collections import deque
S = input()
que = deque(S)
Q = int(input())
flip = False
for i in range(Q):
    query = list(input().split())
    T = int(query[0])
    if T == 1:
        # Sの前後を反転する
        flip = not flip
    else:
        F, C = query[1:]
        F = int(F)
        if F == 1:
            # Sの先頭にCを追加する
            if flip is False:
                que.appendleft(C)
            else:
                que.append(C)
        else:
            # Sの末尾にCを追加する
            if flip is False:
                que.append(C)
            else:
                que.appendleft(C)
if flip is True:
    que.reverse()
print("".join(que))
