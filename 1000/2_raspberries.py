import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    even_count = 0
    ans = float('inf')
    for c in nums:
        if c % k == 0:
            ans = min(ans, 0)
        else:
            ans = min(ans, k - (c%k))
        if c % 2 == 0:
            even_count += 1
    
    if k == 4:
        if even_count >= 2 :
            ans = min(ans, 0)
        if even_count == 1:
            ans = min(ans, 1)
        else:
            ans = min(ans,2)
    print(ans)
