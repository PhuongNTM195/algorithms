def init(n):
    return list(range(1, n + 1))


def print_permute(a):
    for i in a:
        print(i, end=' ')
    print()


def next_permutation(a, n, stop):
    i = n - 2
    # Tim vi tri ma a[i] bat dau nho hon a[i+1]
    while i >= 0 and a[i] > a[i + 1]:
        i -= 1

    # neu i < 0 thi da toi cau hinh cuoi
    if i < 0:
        stop = True
    else:
        k = n - 1
        # tim phan tu nho nhat nhung lon hon a[i]
        while a[k] < a[i]:
            k -= 1
        # doi cho a[i] va a[k] cho nhau
        a[i], a[k] = a[k], a[i]
        l = i + 1
        r = n - 1
        # dao nguoc doan tu l den r
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    return a, stop


def backtrack(i):
    pass


def solve():
    stop = False
    n = 6
    a = init(n)
    check = [True] * n
    print_permute(a)
    while not stop:
        print_permute(a)
        a, stop = next_permutation(a, n, stop)

    # backtrack(a,n)
    pass


solve()
