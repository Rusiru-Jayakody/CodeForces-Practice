import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())

    t1 = b + (-1*(c-b))
    if (a+c) % 2 == 0:
        t2 = (a+c)//2
    else:
        t2 = -1    
    t3 = b + (b-a)
    if t1 > 0 and t1 % a == 0:
        print("YES")
    elif t2 > 0 and t2 % b == 0:
        print("YES")
    elif t3 > 0 and t3 % c == 0:
        print("YES")
    else:
        print("NO")

