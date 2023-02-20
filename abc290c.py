"""
概要
数列AからK要素を選んだ数列Bの合計の最大値を求める
数列Bは以下の条件
1. 0以上以下の全ての整数iが含まれる
2. mが含まれない

解法
全探索はTLEするので工夫する
数列B = set(Aの数列)
0からK+1まで順にループする
1. 数列Bになかった数があれば m = i-1
    0 -> ある
    1 -> ある
    2 -> ある
    3 -> ある
    4 -> ない
    0, 1, 2, 3, 5, 6, 7
2. なければ m = K
    iが全てBに含まれている場合
    K = 3
    0, 1, 2, 3

https://atcoder.jp/contests/abc290/tasks/abc290_c
"""
N, K = map(int, input().split())
A = set(map(int, input().split()))
for i in range(K + 1):
    if not i in A:
        print(i)
        exit()
print(K)
exit()