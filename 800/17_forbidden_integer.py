import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k,x = map(int, input().split())
    ans = []

    if k == 1 or (k == 2 and x == 1 and n % 2 == 1):
        print("NO")    
    else:
        if x != 1:
            for i in range(n):
                ans.append(1)
        else:
            temp = n
            while temp > 0:
                if temp == 3 and k >= 3:
                    ans.append(3)
                    break
                else:
                    ans.append(2)
                    temp -= 2
        print("YES")
        print(len(ans))
        print(*ans)
    