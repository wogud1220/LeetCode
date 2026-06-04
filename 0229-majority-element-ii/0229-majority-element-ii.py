from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        result = []
        for num in nums:
            hash[num] += 1

        n = len(nums)
        divideN = n / 3

        for k, v in hash.items():
            if v > divideN:
                result.append(k)

        return result