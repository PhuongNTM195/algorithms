def sinh_boi_so(a, dem, visited):
    q = [9]
    while dem < 500:
        t = q[0]
        q.pop(0)
        for i in range(1, min(t, 500)+1):
            if t%i == 0 and visited[i] == False:
                visited[i] = True
                a[i] = t
                dem += 1
        q.append(t*10)
        q.append(t*10+9)
    return a


a = [0]*505
visited = [False]*505
dem = 0
a = sinh_boi_so(a, dem, visited)
print(a)