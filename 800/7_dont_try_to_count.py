t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    count = 0
    if s in x:
        print(count)
        continue
    
    while True:
        x += x
        count += 1
        if s in x:
            print(count)
            break
        elif len(x) >= 2*len(s):
            print(-1)
            break

            
    