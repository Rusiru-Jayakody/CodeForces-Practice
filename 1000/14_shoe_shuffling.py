import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(i+1)

    for i in range(1,n):
        if arr[i] == arr[i-1]:
            ans[i],ans[i-1] = ans[i-1],ans[i]
    
    flag = 0
    for i in range(n):
        if ans[i] == i+1:
            flag = 1
            break
    
    if flag == 1:
        print(-1)
    else:
        print(*ans)
