"""
マス目の全探索
ユニークな整数の組を1通りと数える

https://atcoder.jp/contests/abc293/tasks/abc293_c

再帰で全探索を行う
最後まで行ったら要素を削除して戻るのがポイント
"""
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = 0

def dfs(i, j, visited):
  global ans
  if A[i][j] in visited:
    return
  visited.add(A[i][j])
  if i == H - 1 and j == W - 1:
    ans += 1
  if i + 1 < H:
    dfs(i+1, j, visited)
  if j + 1 < W:
    dfs(i, j + 1, visited)
  # print(f"{visited=}, {A[i][j]=}")
  visited.remove(A[i][j])

dfs(0, 0, set())
print(ans)