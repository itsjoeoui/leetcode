#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0, num//2+2):
            if i*i == num:
                return True
            if i*i > num:
                return False
# @lc code=end
