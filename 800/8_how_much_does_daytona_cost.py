t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print("yes" if k in nums else "no")