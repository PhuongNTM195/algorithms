def bieu_thuc_hau_to_1(s):
    s = s.lower()
    st = []
    n = len(s)
    ans = ''
    operators = {'+': 1, '-':1, '*': 2, '/':2, '(': 0}
    for i in range(n):
        if 'z' >= s[i] >= 'a':
            ans += s[i]
        elif s[i] == '(':
            st.append('(')
        elif s[i] == ')':
            x = st[-1]
            st.pop()
            while x != '(':
                ans += x
                x = st[-1]
                st.pop()
        else:
            while len(st) > 0 and operators[s[i]] <= operators[st[-1]]:
                ans += st[-1]
                st.pop()
            st.append(s[i])

    while len(st) > 0:
        x = st[-1]
        ans += x
        st.pop()
    return ans


print(bieu_thuc_hau_to_1("A*B+C*((D-E)+F)/G"))