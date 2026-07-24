class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        n = len(prices)
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
            
            
        
        return max_profit


        # max_profit = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price

        #     profit = price - min_price
        #     if profit > max_profit:
        #         max_profit = profit
            
        
        # return max_profit








