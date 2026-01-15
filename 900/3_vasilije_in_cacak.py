t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    minsum = k*(1+k)//2
    maxsum = k*(2*n-k+1)//2
    if k == 1 and x == 1:
        print("yes")
    elif minsum > x or maxsum < x:
        print("no")
    else:
        print("yes")
