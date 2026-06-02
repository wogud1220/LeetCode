class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            return max(dp)
        a = solve(nums[:-1]) # 마지막 집 선택
        b = solve(nums[1:]) # 첫번째 집 선택
        return max(a,b)