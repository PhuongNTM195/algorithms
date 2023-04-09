def init(k):
    return list(range(1, k + 1))


def print_permute(a):
    for i in a:
        print(i, end=' ')
    print()


def next_permutation(a, n, k, stop):
    i = k-1
    while i >= 0 and a[i] == n-k+i+1:
        i -= 1
    if i < 0:
        stop = True
    else:
        a[i] += 1
        for j in range(i+1, k):
            a[j] = a[j-1] + 1
    return a, stop


def backtrack(a, k):
    pass


def solve():
    stop = False
    n = 5
    k = 3
    a = init(k)
    while not stop:
        print_permute(a)
        a, stop = next_permutation(a,n,k,stop)
        # print_permute(a)
    pass


solve()
