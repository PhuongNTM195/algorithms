n = int(input())
cv = []
for i in range(n):
    a, b = [int(x) for x in input().split()]
    cv.append((a, b))
cv = sorted(cv, key=lambda x: x[1])

count = 1
last = cv[0][1]
i = 1
while i < n:
    if cv[i][0] >= last:
        count += 1
        last = cv[i][1]
    i += 1
print(count)

