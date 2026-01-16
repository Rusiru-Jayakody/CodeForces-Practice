import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    beg = [0] * n
    end = [0] * n
    beg[0], end[-1] = 1,1

    seen = set()
    for i in range(n):
        seen.add(s[i])
        beg[i] = len(seen)
          
    seen.clear()
    for i in range(n-1,-1,-1):
        seen.add(s[i])
        end[i] = len(seen)

    maxx = 0
    for i in range(n-1):
        maxx = max(maxx, beg[i] + end[i+1])

    print(maxx)
