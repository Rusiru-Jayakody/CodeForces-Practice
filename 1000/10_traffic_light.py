import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, c = input().strip().split()
    n = int(n)
    s = input().strip()
    s += s
    next_g = -1
    ans = 0
    for i in range(2*n-1,-1,-1):
        if s[i] == 'g':
            next_g = i
        
        elif s[i] == c and next_g != -1 and i < n:
            ans = max(ans, next_g - i )
    print(ans)

