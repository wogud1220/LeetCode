from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = defaultdict(int)
        result = []
        answer = []
        for num in nums:
            hash[num] += 1

        for a,v in hash.items():
            result.append((a,v))


        result.sort(reverse = True, key = lambda X:X[1])
        
        result = result[:k]
        # print(result)
        for i in range(k):
            print(i)
            answer.append(result[i][0])
        
        return answer
            


        