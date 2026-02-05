import sys
input = sys.stdin.readline
n,d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 0

l,r = 0, n-1
curr = arr[-1]
while l <= r:
    if curr > d:
        count += 1
        r -= 1
        curr = arr[r]
    else:
        curr += arr[r]
        l += 1

print(count)