#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp, rp = 0, len(nums)-1
        while nums[lp] == nums[rp]:
            if lp == rp:
                return nums[lp]
            lp += 1
        rtn = -1
        while lp <= rp:
            mp = lp + (rp-lp)//2
            if nums[mp] <= nums[-1]:
                rtn = nums[mp]
                rp = mp - 1
            else:
                lp = mp + 1
        return rtn
# @lc code=end
