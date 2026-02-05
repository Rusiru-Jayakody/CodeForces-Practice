import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minn = min(arr)
    maxx = max(arr)
    temp = 0
    if arr[0] == minn or arr[-1] == maxx:
        print(maxx-minn)
    else:
        temp = 0
        for i in range(n-1,0,-1):
            temp = max(temp,arr[i-1] - arr[i])
        temp = max(arr[-1] - arr[0], temp)
        print(max(temp, maxx - arr[0], arr[-1]-minn))