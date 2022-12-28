#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rtn: int = nums[0]
        cur: int = -inf

        for n in nums:
            cur = max(cur + n, n)
            rtn = max(rtn, cur)
        return rtn

# @lc code=end
