#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height)-1
        max_water = 0
        while lp < rp:
            lh, rh = height[lp], height[rp]
            max_water = max(min(lh, rh)*(rp-lp), max_water)
            if lh < rh:
                lp += 1
            else:
                rp -= 1
        return max_water
# @lc code=end
