#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        wid = rp
        rtn = 0
        while lp < rp:
            lh = height[lp]
            rh = height[rp]
            rtn = max(rtn, min(lh, rh) * wid)
            if lh > rh:
                rp -= 1
            else:
                lp += 1
            wid -= 1
        return rtn


# @lc code=end
