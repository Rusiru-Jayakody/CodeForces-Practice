import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())

    ann = a
    kat = b

    if c % 2 == 0:
        ann += c // 2
        kat += c // 2
    else:
        ann += ((c//2) + 1)
        kat += c // 2

    if ann > kat:
        print("First")
    else:
        print("Second")