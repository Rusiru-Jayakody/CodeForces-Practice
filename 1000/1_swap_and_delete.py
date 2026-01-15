import sys
t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    ones = s.count('1')
    zeros = s.count('0')
    t = 0

    for c in s:
        if c == '0' and ones > 0:
            t += 1
            ones -= 1
        elif c == '1' and zeros > 0:
            t += 1
            zeros -= 1
        else:
            break
    print(len(s) - t)
        
    
