from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)

        set_1 = set(nums1) #eliminate duplicated
        set_2 = set(nums2)

        nums1 = list(set_1)
        nums2 = list(set_2)

        result = []
        for i in nums1:
            hash_1[i] += 1
        
        for i in nums2:
            if hash_1[i] == 1:
                result.append(i)
        
        return result

        