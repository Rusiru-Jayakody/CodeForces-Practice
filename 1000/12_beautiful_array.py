import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k,b,s = map(int, input().split())
    maxx = ((k*(b+1))-1) + ((n-1)*(k-1))
    minn = b * k

    if s < minn or s > maxx:
        print(-1)
    else:
        ans = []
        rem = s
        if s >= ((k*(b+1))-1):
            ans.append(((k*(b+1))-1))
            rem -= ((k*(b+1))-1)
        else:
            ans.append(s)
            rem = 0       
        x = n - 1
        while x > 0:
            if rem >= k-1:
                ans.append(k-1)
                rem -= (k-1)
                x -= 1
            elif rem == 0:
                ans.append(0)
                x -= 1
            else:
                ans.append(rem)
                rem = 0
                x -= 1
        print(*ans)

