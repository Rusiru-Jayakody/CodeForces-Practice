import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    best = 1
    for i in range(2,math.isqrt(n) + 1):
        if n % i == 0:
            best = n // i
            break
    print(best, n- best)


