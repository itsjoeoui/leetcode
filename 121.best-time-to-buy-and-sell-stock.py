#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1  # lp has to be on the smallest number
        max_price = 0

        while rp < len(prices):
            current_price = prices[rp]-prices[lp]
            if current_price < 0:
                lp = rp
            else:
                max_price = max(max_price, current_price)
            rp = rp + 1
        return max_price

# @lc code=end
