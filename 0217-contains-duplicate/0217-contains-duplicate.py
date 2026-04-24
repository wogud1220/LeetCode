class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        a = set(nums)
        if nums_len != len(a):
            return True
        else:
            return False