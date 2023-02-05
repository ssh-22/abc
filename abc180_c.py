if __name__ == "__main__":
    """
    概要
    約数列挙

    解法
    Nが10**12以上なので全探索で列挙するとTLEになる
    平方根以下までの列挙で計算量をO(N)からO(√N)に減らす

    URL
    https://atcoder.jp/contests/abc180/tasks/abc180_c
    
    入力
    6

    """
    N = int(input())
    divisor = [1]
    i = 1
    while i**2 < N:
        i += 1
        if N % i == 0:
            divisor.append(i)
    ans = set(divisor)
    for d in divisor:
        ans.add(N/d)
    ans = sorted(list(divisor))
    for a in ans:
        print(a)
