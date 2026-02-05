import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    for i in range(n):
        if arr[i] != 0:
            flag += 1
            
    if flag > 0:
        temp = 0
        for i in range(n):
            if temp == flag:
                break
            if arr[i] == 0:
                temp = 0
            else:
                temp += 1
        if temp == flag:
            print(1)
        else:
            print(2)
    else:
        print(0)
