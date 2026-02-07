import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = list(input().strip())
    if s[0] != s[-1]:
        s[0] = s[-1]
    print("".join(s))






