import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minn = float('inf')
    for i in range(n-1,0,-1):
        minn = min(arr[i]-arr[i-1], minn)
    
    if minn < 0:
        print(0)
    else:
        print(minn//2 + 1)