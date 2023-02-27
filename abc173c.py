"""
H行W列のマス目
.の時白、#の時黒
行を何行か選び、列を何列か選ぶ
操作後に黒いマス(#)がK個残る選び方は何通りあるか

https://atcoder.jp/contests/abc173/tasks/abc173_c

bit全探索で行と列を選ぶ
行が選ばれているなら次の行に移動する
列が選ばれているなら次の列に移動する
行、列が選ばれていないかつ黒なら黒の数を数える
黒の数がKと同じならans+=1
ansを出力する
"""
H, W, K = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))
ans = 0
for is_ in range(1 << H):
    for js in range(1 << W):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if is_ >> i & 1:
                    # マスの行が消されているならスキップ
                    continue
                if js >> j & 1:
                    # マスの列が消されているならスキップ
                    continue
                if C[i][j] == "#":
                    # マスが黒の場合
                    cnt += 1
        if cnt == K:
            # 黒がちょうどK個残る
            ans += 1
print(ans)