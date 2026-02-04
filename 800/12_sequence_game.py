import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = []
    q.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1] <= arr[i]:
            q.append(arr[i])
        else:
            q.append(arr[i])
            q.append(arr[i])
    
    print(len(q))
    print(" ".join(map(str,q)))
