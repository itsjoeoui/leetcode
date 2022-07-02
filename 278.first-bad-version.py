#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lp, rp = 1, n
        while lp <= rp:
            mid = lp + (rp-lp)//2
            if isBadVersion(mid) == True:
                rp = mid - 1
            else:
                lp = mid + 1
        return lp
# @lc code=end
