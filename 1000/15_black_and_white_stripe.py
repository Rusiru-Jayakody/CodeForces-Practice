import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s = input().strip()
    white = 0
    minn = float('inf')
    for i in range(k):
        if s[i] == "W":
            white += 1   
    if white == 0:
        print(0)
    else:
        minn = min(minn,white)
        for i in range(k,n):
            x = i-k
            if s[i] == "W" and  s[x] == "B":
                white += 1            
            elif s[i] == "B" and s[x] == "W":
                white -= 1           
            minn = min(minn,white)
        print(minn)
