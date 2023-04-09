
a = [0] * 20


def show(n : int):
    for i in range(0, n):
        print(a[i], end='')
    print()


def binary(n: int, k: int):
    for i in range(0, 2):
        a[k] = i
        if k == n-1:
            show(n)
        else:
            binary(n, k + 1)


def solve():
    n = int(input())
    print("n : ", n)
    binary(n, 0)

solve()
