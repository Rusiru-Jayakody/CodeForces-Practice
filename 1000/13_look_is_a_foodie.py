import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    minn = arr[0]
    maxx = arr[0]
    diff = 2*x

    for i in range(1,n):
        if diff < max(abs(maxx-arr[i]), abs(minn- arr[i])):
            count += 1
            minn = arr[i]
            maxx = arr[i]
        else:
            maxx = max(maxx, arr[i])
            minn = min(minn, arr[i])
    
    print(count)
