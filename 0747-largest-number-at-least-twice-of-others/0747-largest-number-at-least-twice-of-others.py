class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = -1
        second = -1
        index = 0
        for i, num in enumerate(nums):
            if num > max_num:
                second = max_num
                max_num = num
                index = i
            elif num > second:
                second = num
        if max_num >= second * 2:
            return index

        

        return -1