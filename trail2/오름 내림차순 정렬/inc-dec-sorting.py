n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

a = sorted(nums)
print(*a)

nums.sort(reverse = True)
print(*nums)