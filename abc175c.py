"""
概要
数直線でK回移動した後にいる座標の絶対値の最小値

解法
正でも負でも変わらないので正で考える
X - K*D が0以上の場合と負の場合で分けて考える
1. X - K*D >= 0
    X - K*D

2. X - K*D < 0
    1. 残り回数が奇数
        (X - K * D) + D
    2. 残り回数が偶数
        X - K * D

URL
https://atcoder.jp/contests/abc175/tasks/abc175_c
"""
X, K, D = map(int, input().split())
X = abs(X)
if X - K*D >= 0:
    print(X - K*D)
else:
    count = X // D + 1
    current =  X - count * D
    remaining = K - count
    if remaining:
        if remaining % 2 == 0:
            print(abs(current))
        else:
            print(abs(current + D))
    else:
        print(abs(current))