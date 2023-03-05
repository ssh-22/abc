"""
整数Nを買うためにはA*N+B*d(N)が必要
d(N)はNの桁数
所持金がX円の時買うことができる最も大きい整数を求める
1つも買うことができない場合は0を出力する
1<=A<=10**9
1<=B<=10**9
1<=X<=10**9

https://atcoder.jp/contests/abc146/tasks/abc146_c

10 7 100
N -> 10*N+7*len(N)円
1 -> 10*1+7*1=17円
9 -> 10*9+7*1=104円
10 -> 10*10+7*2=114円
"""
A, B, X = map(int, input().split())
def price(N):
    """
    整数Nを買うためのコストを求める
    """
    global A, B
    return A*N+B*len(str(N))
# 二分探索
# 探索範囲外
left = 1
right = 10**20
# 整数1も買えない場合
if X < price(1):
    print(0)
    exit()
# right=6, left=5の時終了
while 1 < right-left:
    # 真ん中の数
    N = (left+right) // 2
    # 真ん中の数を買える場合、真ん中の数を左端にして、真ん中より右を探索する
    if price(N) <= X:
        # 買うことができる最大の数
        left = N
    # 真ん中の数を買えない場合、真ん中を右端にして真ん中より左を探索する
    else:
        # 探索範囲の右端
        right = N
# 10**9より大きい数が買える場合、制約により、10**9を買える数にする
if 10**9 < left:
    left = 10**9
print(left)