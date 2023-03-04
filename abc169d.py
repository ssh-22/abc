"""
正の整数Nに対して以下の操作を繰り返し行う
1. 以下の条件を満たす正の整数zを選ぶ
    1. 素数pと正の整数eを用いて z = p**eと表せる
    2. Nがzで割り切れる
    3. 以前の操作で選んだどの整数とも異なる
2. NをN/zで置き換える
最大で何回操作を行うことができるか求める
1 <= N <= 10**12

https://atcoder.jp/contests/abc169/tasks/abc169_d

N = 24
ex.
1. z = 2
    1. 2 = 2**1
    2. 24 % 2 = 0
    3. 2 not in Z 
    4. N -> 12
z = 3
    1. 3 = 3**1
    2. 24 % 3 = 0
    3. not in Z 
    4. N -> 4
z = 4(N -> 1)
    1. 4 = 2**2
    2. 24 % 4 = 0
    3. not in Z 
    4. N -> 4
"""
import math

def prime_factorize(N):
    """
    素因数分解する因数をリストで返す

    Args:
        N (int): 素因数分解する対象の数

    Returns:
        list: 因数のリスト

    Examples:
        24を素因数分解すると(2**3)*3

        >>> print(prime_factorize(24))
        [2, 2, 2, 3]
    """
    # 定義により1は素数ではない
    if N == 1:
        return []
    prime_lst = []
    # i <= √Nの間(i>√Nまで, i**i <= N)
    # 4の素因数分解で√4=2より大きい3を試しても意味がないのと同じ
    i = 2
    while i * i <= N:
        if N % i == 0:
            prime_lst.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_lst.append(N)
    return prime_lst

N = int(input())
ans = 0
prime_set = set(prime_factorize(N))
for p in prime_set:
    for e in range(1, 10**10):
        z = p ** e
        if N % z == 0:
            ans += 1
            N //= z
        else:
            # 割り切れないならeのループを抜けて次の素数にいく
            break
print(ans)