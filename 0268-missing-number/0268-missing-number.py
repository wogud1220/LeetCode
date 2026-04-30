class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # no sort
        max_val = len(nums)
        a = (max_val * (max_val + 1)) // 2 # a= 6
        sum_nums = sum(nums) # 4
        return a - sum_nums
        