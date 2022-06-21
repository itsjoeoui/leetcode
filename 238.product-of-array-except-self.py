#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,3,5,4,7]
        # >>> list(accumulate(nums, add))
        # [1, 4, 9, 13, 20]
        # >>> list(accumulate(nums, mul))
        # [1, 3, 15, 60, 420]

        prev = list(accumulate(nums, mul))
        after = list(accumulate(nums[::-1], mul))

        result = [1]*len(nums)

        for i in range(len(nums)):
            result[i] = (prev[i-1] if i != 0 else 1) * \
                (after[-i-2] if i != len(nums)-1 else 1)
        return result

        #      prev    after
        # 0:    None      -2
        # 1:    0         -3
        # 2:    1         -4
        # 3:    2       None
        # @lc code=end
