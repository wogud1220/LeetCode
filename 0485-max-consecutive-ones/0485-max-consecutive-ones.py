class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt_max = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt_max = max(cnt, cnt_max)
                cnt = 0

        return max(cnt_max,cnt)