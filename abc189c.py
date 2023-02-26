"""
N枚の皿が一列に並ぶ
左からi番目の皿にはAi個のみかんが置かれている
以下の3条件を満たす整数の組を1つ選ぶ

1. 1<=l<=r<= N
2. 1<=x
3. l以上r以下の全ての整数iについて、x<=Ai

lからr番目まで(両端含む)の全ての皿からみかんをx個ずつとって食べる
食べられる最大のみかんの個数を求める

1<=N<=10**4
1<=Ai<=10**5

https://atcoder.jp/contests/abc189/tasks/abc189_c

1. 左端(l)を決める
2. 右端(r)を決める
3. xを求める(最初はl, A[r]で更新する)
4. みかんの最大数(x*(r-l+1))を更新する

"""
N = int(input())
A = list(map(int, input().split()))
i = 0
ans = 0
for l in range(N):
    x = A[l]
    for r in range(l, N):
        x = min(x, A[r])
        ans = max(ans, x*(r-l+1))
print(ans)