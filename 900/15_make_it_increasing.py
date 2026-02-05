import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(0)
    else:
        seen = set()
        flag = 0
        count = 0
        seen.add(arr[-1])
        for i in range(n-1,0,-1):
            temp = arr[i-1]
            while temp >= arr[i] and temp != 0:
                temp //= 2
                count += 1
            arr[i-1] = temp
            if arr[i-1] in seen:
                flag = 1
                break
            seen.add(arr[i-1])
        if flag == 1:
            print(-1)
        else:
            print(count)
