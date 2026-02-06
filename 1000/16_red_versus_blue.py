import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,r,b = map(int, input().split())
    x = r // (b+1)
    y = r % (b+1)
    ans = []
    for i in range(b+1):
        ans.extend(['R']*x)
        if y > 0:
            ans.append('R')
            y -= 1
        if i != b:
            ans.append('B')
    print("".join(ans))



        
        

