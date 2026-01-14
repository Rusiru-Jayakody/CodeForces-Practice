from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    freq = Counter(nums)
    if len(freq) == 1:
        print("yes")
    elif len(freq) > 2:
        print("no")
    else:
        a,b = freq.values()
        print("yes" if abs(a-b) < 2 else "no")
  
