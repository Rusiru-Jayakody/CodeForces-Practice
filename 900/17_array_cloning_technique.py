import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxx = 0
    curr = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            maxx = max(maxx,curr)
            curr = 1
        else:
            curr += 1
    maxx = max(maxx,curr)
    count = n - maxx
    temp = count
    while temp > 0:
        count += 1
        temp -= maxx
        maxx *= 2
    
    print(count)