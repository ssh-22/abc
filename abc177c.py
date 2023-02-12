"""
概要


解法
全探索でやるとTLEになるので工夫して計算量を減らす
1 2 3
1 * 2 + 1 * 3 + 2 * 3
= 1 * (2 + 3) + 2 * 3
1 2 3 4
1 * 2 + 1 * 3 + 1 * 4 + 2 * 3 + 2 * 4 + 3 * 4
= 1 * (2 + 3 + 4) + 2 * (3 + 4) + 3 * 4

a b c d
= a * (b + c + d) + b * (c + d) + c * d

mod(10**9+7)

URL
https://atcoder.jp/contests/abc177/tasks/abc177_c
"""
N = int(input())
A = list(map(int, input().split()))
ans = 0
sum_a = sum(A)
for i in range(N):
    sum_a -= A[i]
    ans += A[i] * sum_a
    ans %= 10 ** 9 + 7
print(ans)