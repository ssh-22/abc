if __name__ == "__main__":
    """
    概要
    1円ずつ増やして全探索するとTLEになる
    
    解法
    全探索だとTLEするのでまず初めにK円分だけ進むのがポイント
    1. 友達を村順に昇順ソートする
    2. Kだけ進む(now += K)
    3. K以下の村Aiについて、Biだけ進む(now += Bi)
    4. now以下の友達がいなければnowを出力して終了

    URL
    https://atcoder.jp/contests/abc203/tasks/abc203_c

    入力
    2 3
    2 1
    5 10
    """
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        A, B = map(int, input().split())
        friends.append([A, B])
    friends.sort()
    now = 0
    now += K
    for i in range(N):
        village = friends[i][0]
        money = friends[i][1]
        if village <= now:
            now += money
        else:
            break
    print(now)