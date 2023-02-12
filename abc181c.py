if __name__ == "__main__":
    """
    概要
    3点を通る直線が存在するか
    
    解法
    2点を通る直線の公式に3点目の点を代入して成り立つか確認する
    y - y1 = (y2 - y1)/(x2 - x1) * (x - x1)
    (y - y1) * (x2 - x1) = (y2 - y1) * (x - x1)
    (y3 - y1) * (x2 - x1) = (y2 - y1) * (x3 - x1)
    3点の組み合わせの列挙はforループの3重ループで行う
    10**2**3なので2秒以内に間に合う

    URL
    https://atcoder.jp/contests/abc181/tasks/abc181_c

    入力例
    4
    0 1
    0 2
    0 3
    1 1
    
    出力例
    Yes
    """
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                is_on_same_line = (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)
                if is_on_same_line:
                    print("Yes")
                    exit()
    print("No")