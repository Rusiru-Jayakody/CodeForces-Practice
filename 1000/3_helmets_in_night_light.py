import sys
import heapq
t = int(sys.stdin.readline())
for _ in range(t):
    n, p = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    heap = []
    for i in range(n):
        heapq.heappush(heap,(b[i],a[i]))
    
    count = 1
    cost = p
    while heap and count < n:
        u,v = heapq.heappop(heap)
        if u < p:
            cost += (u * min(v, n - count))
            count += min(v, n - count)
            
    if count >= n:
        print(cost)
    else:
        cost += p*(n-count)
        print(cost)