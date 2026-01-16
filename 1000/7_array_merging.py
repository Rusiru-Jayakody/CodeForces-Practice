import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    def builddict(arr):
        d = defaultdict(int)
        temp = 1
        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]:
                d[arr[i-1]] = max(d[arr[i-1]],temp)
                temp = 1
            else:
                temp += 1
        d[arr[-1]] = max(d[arr[-1]],temp)
        return d
    
    d1 = builddict(a)
    d2 = builddict(b)

    maxx = 0
    for k in set(d1)|set(d2):
        maxx = max(maxx, d1[k] + d2[k])

    print(maxx)