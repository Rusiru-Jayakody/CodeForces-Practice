import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    minn = float('inf')
    ans = [0,0]
    for i in range(1,n//2+1):
        a , b = i , n - i
        lcm = (a*b)//math.gcd(a,b)
        if lcm < minn:
            minn = lcm
            ans[0] = a
            ans[1] = b
    
    print(ans[0], ans[1])

