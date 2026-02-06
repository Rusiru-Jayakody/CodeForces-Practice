import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    summ = n + 1
    for i in range(n):
        ans.append(summ - arr[i])
    print(*ans)