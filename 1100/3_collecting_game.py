import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)
    dp = {}

    for i in range(n):
        d[a[i]].append(i)

    a.sort()
    ans = [0] * n

    count = 0
    summ = 0
    for i in range(n):
        if ans[i] != 0:
            continue
        summ += a[i] * len(d[a[i]])

        
