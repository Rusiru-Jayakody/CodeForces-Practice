t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    gas = list(map(int, input().split()))
    maxx = 0
    for i in range(n-1):
        maxx = max(maxx,gas[i+1] - gas[i])
    
    maxx = max(maxx, 2*(x-gas[-1]),gas[0])
    print(maxx)

