import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    temp = 1
    maxl = 0
    for i in range(1,n):
        if abs(arr[i] -arr[i-1]) <= k:
            temp += 1
        else:
            maxl = max(maxl,temp)
            temp = 1
    
    maxl = max(maxl, temp)
    print(n-maxl)

