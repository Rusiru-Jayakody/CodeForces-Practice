import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k,p = map(int, input().split())
    temp = list(map(int, input().split()))
    total = 0
    temp_count = 0
    for i in range(n):
        if temp[i] > p:
            temp_count = 0
            continue
        temp_count += 1
        if temp_count >= k:
            total += 1 + (temp_count - k)
    
    print(total)
