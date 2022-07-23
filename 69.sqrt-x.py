#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        rlt = -1
        while l <= r:
            m = l + (r-l)//2
            if m * m <= x:
                rlt = m
                l = m + 1
            else:
                r = m -1
        return rlt
        
# @lc code=end

