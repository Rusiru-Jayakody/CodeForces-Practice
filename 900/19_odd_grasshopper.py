import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x,n = map(int, input().split())

    c = (n+3) // 4
    y = n % 4
    ans = 0

    if x % 2 == 1:
        if y == 1:
            ans = x + (4*(c-1)+1)
        elif y == 2:
            ans = x - 1
        elif y == 3:
            ans = x - (4*c)
        else:
            ans = x
    else:
        if y == 1:
             ans = x-(4*(c-1)+1)
        elif y == 2:
            ans = x + 1
        elif y == 3:
            ans = x + (4*c)
        else:
            ans = x

    print(ans)

