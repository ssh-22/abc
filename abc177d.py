"""
N人の人
友達の情報がM個
XとYが友達かつYとZが友達ならXとZも友達
同じグループの中に友達がいないようにするには最小でいくつのグループに分ければ良いか

https://atcoder.jp/contests/abc177/tasks/abc177_d

UnionFind
1 2
3 4
5 1
{1, 2, 5}
{3, 4}
同じグループの中に友達がいないようにする
最低3グループ必要
全てのグループごとのノードを取得し、最大のグループの要素数が答えになる
"""
from library.union_find import UnionFind

N, M = map(int, input().split())
ans = 0
uf = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    # 0index
    A -= 1
    B -= 1
    uf.unite(A, B)
ans = 0
for group_size in uf.group_members.values():
    ans = max(ans, len(group_size))
print(ans)