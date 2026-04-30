from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = defaultdict(int)

        for num in nums1:
            hash[num] += 1
        result = []

        for num in nums2:
            if hash[num] > 0:
                result.append(num)
                hash[num] -= 1
        return result