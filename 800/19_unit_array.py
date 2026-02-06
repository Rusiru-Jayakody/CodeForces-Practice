import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    plus = 0
    for i in range(n):
        if arr[i] == 1:
            plus += 1
    minus = n - plus
    count = 0

    if minus > plus:
        count += math.ceil(abs(plus-minus)/2)
        minus -= count
    
    if minus % 2 == 1:
        count += 1

    print(count)
    

        
    

