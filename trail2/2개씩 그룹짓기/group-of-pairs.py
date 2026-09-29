n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
i = 0
j = len(nums) - 1
m = nums[i] + nums[j]

i = 1
j = len(nums) - 2
while (i<j):
    m = max(nums[i]+nums[j], m)
    i += 1
    j -=1

print(m)

