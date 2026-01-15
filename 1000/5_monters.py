import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = arr[i] % k
    heap = []
    ans = []
    for i in range(n):
        if arr[i] == 0:
            ans.append(i+1)
        else:
            heapq.heappush(heap,(-arr[i],i+1))
    
    while heap:
        s, i = heapq.heappop(heap)
        ans.append(i)

    print(" ".join(map(str,ans)))
   

