from collections import Counter
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    counter = Counter(s)
    count = 0
    for v in counter.values():
        if v % 2 == 1:
            count += 1
    
    print("no" if (count - k > 1) else "yes")