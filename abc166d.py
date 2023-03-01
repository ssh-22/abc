"""
A**5 - B**5 = Xを満たす整数の組を1つ示す
1 <= X <= 10**9

https://atcoder.jp/contests/abc166/tasks/abc166_d

1 <= A**5 - B**5 <= 10**9
1 <= C**5 - (C-1)**5 <= 10**9
1 <= C**4 + ... <= 10**9
1 <= (10**3)**4 + ... <= 10**9
10**3まで探せば十分
"""
X = int(input())
for A in range(-10**3, 10**3):
    for B in range(-10**3, 10**3):
        if A**5 - B**5 == X:
            print(*[A, B])
            exit()
