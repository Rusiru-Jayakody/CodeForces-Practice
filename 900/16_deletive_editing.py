import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s,t = input().strip().split()
    counter = [0] * 26
    for c in t:
        counter[ord(c)-ord('A')] += 1
    res = []
    for i in range(len(s)-1,-1,-1):
        if counter[ord(s[i])-ord('A')] > 0:
            counter[ord(s[i])-ord('A')] -= 1
            res.append(s[i])
    
    res.reverse()
    if t == "".join(res):
        print("YES")
    else:
        print("NO")
