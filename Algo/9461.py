t = int(input())

for _ in range(t):
    n = int(input())
    p = [0]*(101)
    p[1], p[2], p[3] = 1, 1, 1
    p[4], p[5] = 2, 2
    if n>=6:
        for i in range(6,n+1):
            p[i] = p[i-5] + p[i-1]
    print(p[n])      