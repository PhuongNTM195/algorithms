def luythua(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        p = luythua(a, b/2, mod)
        return (p*p)%mod
    else:
        p = luythua(a, b-1, mod)
        return (a*p)%mod


mod = 10**9 + 7
print(luythua(2,5,mod))

