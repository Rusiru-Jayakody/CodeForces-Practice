import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        array.append(arr)
    min_first_element = float('inf')
    min_second_element = float('inf')
    summ = 0

    for i in range(n):
        min_first_element = min(min_first_element, array[i][0])
        min_second_element = min(min_second_element, array[i][1])
        summ += array[i][1]
    
    summ -= min_second_element
    summ += min_first_element
    print(summ)

    