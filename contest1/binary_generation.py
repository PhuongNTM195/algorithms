def init():
    n = int(input())
    return n


def print_lst(a):
    for j in a:
        print(j, end='')
    print()


def generate(a, n, stop):
    i = n-1
    while i >= 0 and a[i] == 1:
        i -= 1
    if i < 0:
        stop = True
    else:
        a[i] = 1
        for j in range(i + 1, n):
            a[j] = 0
    return a, stop

def backtrack(a, i, n):
    for j in range(0, 2):
        a[i] = j
        if i == n-1:
            print_lst(a)
        else:
            backtrack(a, i+1, n)


def solve():
    n = 4
    a = [0]*n
    stop = False
    while not stop:
        print_lst(a)
        a, stop = generate(a,n,stop)
    # cach sinh binh thuong
    # while True:
    #     print_lst(a)
    #     i = n-1
    #     a,i = generate(a,i,n)
    #     if i == -1:
    #         break

    ## cach sinh quay lui
    # backtrack(a,0,n)
    pass


solve()