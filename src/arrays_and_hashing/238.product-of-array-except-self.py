#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [1] * size

        left = 1
        right = 1

        for i in range(size):
            output[i] *= left
            output[~i] *= right
            left *= nums[i]
            right *= nums[~i]

        return output

        # @lc code=end
