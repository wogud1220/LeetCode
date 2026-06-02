import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums) # distinct
        # nums = list(nums) # make list again
        if len(nums) < 3:
            return max(nums)
        else:
            heap = []
            for num in nums:
                heapq.heappush(heap, num)
                if len(heap) > 3:
                    heapq.heappop(heap)

            return heap[0]





