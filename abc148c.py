import math


if __name__ == "__main__":
    """
    概要
    最小公倍数を出力する
    
    解法
    最小公倍数
    A * B = 最大公約数 * 最小公倍数
    最小公倍数 = A * B / 最大公約数
    12 * 18 = 6 * 36

    URL
    https://atcoder.jp/contests/abc148/tasks/abc148_c

    入力例
    2 3
    
    出力例
    6

    """
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    lcm = A * B // gcd
    print(lcm)