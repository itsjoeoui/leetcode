#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lp, rp = 0, len(nums) - 1
        while nums[lp] == nums[rp]:
            if lp == rp:
                break
            lp += 1

        while lp <= rp:
            mp = lp + (rp - lp) // 2
            if target == nums[mp]:
                return True
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
        return False
# @lc code=end
