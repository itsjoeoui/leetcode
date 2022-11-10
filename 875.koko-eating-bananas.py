#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            if sum(-(-p // m) for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l
# @lc code=end
