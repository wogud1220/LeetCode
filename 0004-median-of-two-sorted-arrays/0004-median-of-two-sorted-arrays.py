class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        a = 0
        odd = False
        even = False
        if len(arr) % 2 == 1:
            odd = True
        else:
            even = True

        if odd == True:
            a = (len(arr) // 2) +1
            return arr[a-1]
        else:
            a = (len(arr) // 2)
            return (arr[a] + arr[a-1]) /2
    
        return a
        