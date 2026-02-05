import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    c = []
    b = []
    if arr[0] == arr[-1]:
        print(-1)
    else:
        for i in range(n):
            if arr[i] == arr[0]:
                b.append(arr[i])
            else:
                c.append(arr[i])
        
        print(len(b), len(c))
        print(" ".join(map(str,b)))
        print(" ".join(map(str, c)))

