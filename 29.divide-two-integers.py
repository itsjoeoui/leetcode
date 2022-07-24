#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647  # Lol I give up
        lp, rp = 0, abs(dividend)
        rtn = 0

        while lp <= rp:
            mp = lp + (rp - lp)//2
            if mp * abs(divisor) <= abs(dividend):
                rtn = mp
                lp = mp+1
            else:
                rp = mp-1

        if (divisor > 0) == (dividend > 0):
            return rtn
        else:
            return -rtn


# @lc code=end
