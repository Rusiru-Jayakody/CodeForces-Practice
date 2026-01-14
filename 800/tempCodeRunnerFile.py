t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(len(nums)-1):
        if nums[i] > nums[i+ 1] and k <= 1:
            print("NO")
    
    print("YES")
        