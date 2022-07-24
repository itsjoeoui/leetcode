#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lp, rp = 0, len(nums)-1
        rtn = [-1, -1]
        while lp <= rp:
            mp = lp + (rp-lp)//2
            if nums[mp] > target:
                rp = mp - 1
            elif nums[mp] == target:
                rtn[0] = mp
                rp = mp - 1
            else:
                lp = mp + 1
        rp = len(nums)-1
        while lp <= rp:
            mp = lp + (rp-lp)//2
            if nums[mp] < target:
                lp = mp + 1
            elif nums[mp] == target:
                rtn[1] = mp
                lp = mp + 1
            else:
                rp = mp - 1
        return rtn
# @lc code=end
