t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print("yes" if nums[0] == 1 else "no")