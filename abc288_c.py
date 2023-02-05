from library.union_find import UnionFind


if __name__ == "__main__":
    """
    https://atcoder.jp/contests/abc288/tasks/abc288_c
    入力
    6 7
    1 2
    1 3
    2 3
    4 2
    6 5
    4 6
    4 5
    """
N, M = map(int, input().split())
ans = 0
uf = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    if not uf.same(a, b):
        uf.unite(a, b)
    else:
        ans += 1
print(ans)

