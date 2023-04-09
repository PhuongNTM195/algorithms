a = [0] * 20
f = [0] * 20


def show(k: int):
    for i in range(1, k+1):
        print(a[i], end='')
    print()


def to_hop(n: int, k: int, i: int):
    for j in range(i, n + 1):
        if f[j] == 0 and j > a[i-1]:
            a[i] = j
            f[j] = 1
            if k == i:
                show(k)
            else:
                to_hop(n, k, i + 1)
            f[j] = 0


def solve():
    n = int(input())
    k = int(input())
    print("n : ", n)
    print("k : ", k)
    to_hop(n, k, 1)


solve()
