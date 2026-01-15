import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    maxl = 0
    temp = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            temp += 1
        else:
            maxl = max(maxl,temp)
            temp = 1
    maxl = max(temp, maxl)
    print(maxl+1)
