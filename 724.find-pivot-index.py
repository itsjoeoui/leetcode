#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)
        for i, v in enumerate(nums):
            lsum += v
            if lsum == rsum:
                return i
            rsum -= v
        return -1
# @lc code=end
