"""
公差1の等差数列
総和がNであるものはいくつあるか

https://atcoder.jp/contests/abc190/tasks/abc190_d

等差数列の和
1/2*項数*(初項+末項)=和
1/2*(B-A+1)*(A+B)=N
(B-A+1)*(A+B)=2N
x*y=2N
x=B-A+1
y=A+B
2N=x*y(x,yは整数)と分解した時、x=B-A+1,y=A+Bとして、
ABともに整数となるx,yの組み合わせはいくつあるか

x+y=2B+1
B=1/2*(x+y)

x-y=-2A+1
2A=-x+y+1
A=1/2*(y-x+1)

A=1/2*(y-x+1)
B=1/2*(x+y)
y-x+1,x+yがともに偶数
x,yの一方が奇数かつもう一方が偶数
x,yを2で割った余りが異なる組み合わせ

2N=x*y(x,yは整数)
2nを1から√2nまで試し割りする
xを偶数とするとy=2N//x
x,yの一方が奇数かつもう一方が偶数
x,yを2で割った余りが異なる組み合わせ
逆のパターン(3,4なら4,3)も考えて+2にする
"""
import math
N = int(input())
ans = 0
for i in range(1, int(math.sqrt(2*N))+1):
    if 2 * N % i == 0:
        x = i
        y = 2 * N // x
        if x % 2 != y % 2:
            ans += 2
print(ans)