import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a,b,n = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))
    maxx = a-1
    maxtime = b
    for time in times:
        maxtime += min(maxx, time)
    print(maxtime)