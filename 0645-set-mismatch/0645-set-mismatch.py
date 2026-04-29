from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        result = []
        for num in nums:
            hash[num] += 1
            if hash[num] == 2:
                result.append(num)

        for i in range(1, len(nums)+1):
            if hash[i] == 0:
                result.append(i)

        return result
            
            
        