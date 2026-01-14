t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    flag = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+ 1] and k <= 1:
            print("NO")
            flag = 1
            break
    
    if flag == 0:
        print("YES")
        