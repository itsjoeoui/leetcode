#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lp, rp = i+1, len(nums)-1
            target = 0 - nums[i]

            while lp < rp:
                cur = nums[lp] + nums[rp]

                if cur == target:
                    rtn.append([nums[i], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp-1]:
                        rp -= 1
                    lp += 1
                    rp -= 1

                elif cur < target:
                    lp += 1
                else:
                    rp -= 1

        return rtn

# @lc code=end
