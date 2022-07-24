#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mp = lp + (rp-lp) // 2
            if nums[mp] > nums[mp+1]:
                rp = mp
            elif nums[mp] < nums[mp+1]:
                lp = mp + 1
        return rp
# @lc code=end
