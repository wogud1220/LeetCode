class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = list(zip(names, heights))

        result.sort(key = lambda X:X[1], reverse= True)
        
        answer = [human[0] for human in result]

        return answer