if __name__ == "__main__":
    """
    概要
    3の倍数を作るために最小の消す桁数を求める

    解法
    3の倍数 = 各桁の合計が3で割り切れる数

    1. 各桁の合計 % 3 == 0
    369
    0桁消す

    2. 各桁の合計 % 3 == 1
        1. 余りが1の桁が存在する
        334
        x 4
        1桁消す
        2桁以上の場合のみ

        2. 余りが1の桁が存在しない
        余りが2の桁が2つ存在する
        553
        2桁消す
        3桁以上の場合のみ
    
    3. 各桁の合計 % 3 == 2
        1. 余りが2の桁が存在する
        533
        x 5
        1桁消す
        2桁以上の場合のみ

        2. 余りが1の桁が存在しない
        余りが2の桁が2つ存在する
        443
        x 44
        2桁消す
        3桁以上の場合のみ
    
    URL
    https://atcoder.jp/contests/abc182/tasks/abc182_c

    入力
    35

    出力
    1
    """
    N = input()
    sum_of_digits = sum(list(map(int, list(N))))
    has_reminder_of_one = False
    has_reminder_of_two = False
    above_two_digits = len(N) >= 2
    above_three_digits = len(N) >= 3

    for i in range(len(N)):
        digit = int(N[i])
        if digit % 3 == 1:
            has_reminder_of_one = True
        elif digit % 3 == 2:
            has_reminder_of_two = True
    if sum_of_digits % 3 == 0:
        print(0)
        exit()
    elif sum_of_digits % 3 == 1:
        if has_reminder_of_one:
            if above_two_digits:
                print(1)
                exit()
            else:
                print(-1)
                exit()
        else:
            if above_three_digits:
                print(2)
                exit()
            else:
                print(-1)
                exit()
    elif sum_of_digits % 3 == 2:
        if has_reminder_of_two:
            if above_two_digits:
                print(1)
                exit()
            else:
                print(-1)
                exit()
        else:
            if above_three_digits:
                print(2)
                exit()
            else:
                print(-1)
                exit()
