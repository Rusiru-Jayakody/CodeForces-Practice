import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sums = [0] * (n+1)
    for i in range(n):       
        prefix_sums[i+1] = prefix_sums[i] + arr[i]
    
    summ = prefix_sums[n]

    for _ in range(q):
        l,r,k = map(int, input().split())
        temp_sum = prefix_sums[r] - prefix_sums[l-1] 
        new_sum = summ - temp_sum + (k*(r-l+1))
        
        print("yes" if new_sum % 2 == 1 else "no")