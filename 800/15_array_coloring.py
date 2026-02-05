import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for c in arr:
        if c%2 == 1:
            count += 1
    if count % 2 == 0:
        print("YES")
    else:
        print("NO")