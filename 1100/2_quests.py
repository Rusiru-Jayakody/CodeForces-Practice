import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    summ = 0
    maxx = 0
    ans = 0

    for i in range(min(n,k)):
        summ += a[i]
        maxx = max(maxx, b[i])
        ans = max(ans, summ + (k-i-1)*maxx)

    print(ans)