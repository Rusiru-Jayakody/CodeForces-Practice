import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    g = 0
    for i in range(n):
        g = math.gcd(g, abs(nums[i]-i-1))
    print(g)
    
