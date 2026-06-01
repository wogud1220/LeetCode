class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        answer = 0
        for price in prices:
            if price < min_price: # 7 < 7, # 1 < 7
                min_price = price # min = 1

            profit = price - min_price # 1 - 1 = 0


            if profit > answer:
                answer = profit


        return answer

