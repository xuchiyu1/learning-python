class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0


        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
"""
LeetCode 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Type: Array / Greedy

Key Idea:
- Maintain the lowest price seen so far.
- At each day, compute profit if selling today.
- Update the maximum profit.
- Single pass solution.

Time: O(n)
Space: O(1)

Reflection:
- Initially seems like a two-loop problem.
- Realization: only the historical minimum matters.
- This is a classic “state maintenance” pattern.
"""
