class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1e9
        result_price = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                result_price = max(result_price, price - min_price)

        return result_price