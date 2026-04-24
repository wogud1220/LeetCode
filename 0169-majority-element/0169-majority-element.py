class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                result = num
                cnt +=1
            elif num == result:
                cnt+=1
            else:
                cnt-=1
        return result