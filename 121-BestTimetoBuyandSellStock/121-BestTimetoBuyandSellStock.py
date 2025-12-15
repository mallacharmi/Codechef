# Last updated: 12/15/2025, 4:45:41 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price=float('inf')
4        max_profit=0
5        for price in prices:
6            if price < min_price:
7                min_price=price
8            else:
9                max_profit=max(max_profit,price-min_price)
10        return max_profit
11        