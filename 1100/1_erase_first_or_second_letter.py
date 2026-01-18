import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    sett = set()
    total = 0
    for c in s:
        sett.add(c)
        total += len(sett)
    
    print(total)