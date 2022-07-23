#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums)-1
        
        while lp <= rp:
            mp = lp + (rp - lp) // 2
            if target == nums[mp]:
                return mp       
            if nums[mp] <= nums[-1]:
                if target > nums[-1]:
                    rp = mp - 1
                else:
                    if nums[mp] > target:
                        rp = mp - 1
                    else:
                        lp = mp + 1
            else:
                if target <= nums[-1]:
                    lp = mp + 1
                else:
                    if nums[mp] > target:
                        rp = mp - 1
                    else:
                        lp = mp + 1       
        return -1 
# @lc code=end

