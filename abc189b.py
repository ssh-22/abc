if __name__ == "__main__":
    """
    概要
    浮動小数点の誤差

    解法
    小数点の計算にならないように100倍する
    
    URL
    https://atcoder.jp/contests/abc180/tasks/abc180_c
    
    入力
    2 15
    200 5
    350 3

    出力
    2

    """
    N, X = map(int, input().split())
    X = 100 * X
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P
        if X < 0:
            print(i+1)
            exit()
    print(-1)
