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
