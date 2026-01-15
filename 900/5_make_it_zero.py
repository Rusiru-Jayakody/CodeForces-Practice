import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    if n % 2 == 0:
        print(2)
        print(1,n)
        print(1,n)
    else:
        print(4)
        print(1,n-1)
        print(1,n-1)
        print(n-1,n)
        print(n-1,n)


