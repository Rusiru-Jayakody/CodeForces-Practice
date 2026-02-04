import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

minn = float('inf')
for c in arr:
    minn = min(abs(c),minn)

print(minn)
