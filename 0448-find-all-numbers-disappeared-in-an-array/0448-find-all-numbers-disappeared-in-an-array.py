class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        result = []
        for i in range(1, len(nums)+1):
            if hash[i] == 0:
                result.append(i)
        return result
            