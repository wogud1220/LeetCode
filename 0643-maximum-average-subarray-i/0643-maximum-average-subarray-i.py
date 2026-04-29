class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = []
        i = 0
        j = k
        window_sum = sum(nums[:k]) # 0:3 -> 0,1,2 index
        max_sum = window_sum
        while j< len(nums):
            window_sum = window_sum + nums[j] - nums[i]
            max_sum = max(max_sum, window_sum)
            j += 1
            i += 1
        
        return round(max_sum / k, 5)
        
