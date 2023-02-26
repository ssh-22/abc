"""
同じ座標にいたことがあるか求める

https://atcoder.jp/contests/abc291/tasks/abc291_c

リストから検索するとTLEになるため、タプルのSetを利用する
座標の移動はx, yだけ加算し、Setの更新は最後にまとめて行う
"""
N = int(input())
S = list(input())
x = 0
y = 0
history = {(x, y)}
for i in range(N):
  if S[i] == "R":
    x += 1
  if S[i] == "L":
    x -= 1
  if S[i] == "U":
    y += 1
  if S[i] == "D":
    y -= 1
  if (x, y) in history:
    print("Yes")
    exit()
  history.add((x, y))
print("No")
