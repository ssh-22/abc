"""
概要
1以上N以下の整数で2以上の整数a, bを用いてa**bと表せないものはいくつあるか？

解法
Nからa**bと表せる数のsetの合計を引く
1 <= N <= 10**10
a, bをそれぞれ固定して、最大の閾値を見つける
1. a = 2で固定
    2**b <= 10**10
    b <= log 2 10**10
    b <= 33.21
2. b = 2で固定
    a ** 2 <= 10**10
    a <= 10**5

URL
https://atcoder.jp/contests/abc193/tasks/abc193_c
"""
N = int(input())
expressed = set()
for a in range(2, 10**5):
    for b in range(2, 34):
        if a**b <= N:
            expressed.add(a**b)
        else:
            break
print(N - len(expressed))
