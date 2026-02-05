import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1 or n < 4:
        print(-1)
    else:
        maxx = 0
        minn = 0
        x = 0
        temp = n
        while temp % 4 != 0:
            x += 1
            temp -= 6
        maxx = (temp // 4) + x

        x = 0
        temp = n
        while temp % 6 != 0:
            x += 1
            temp -= 4
        minn = (temp // 6) + x

        print(minn, maxx)

