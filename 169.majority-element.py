#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

from typing import List

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1

            elif count == 0:
                major = nums[i]
                count += 1
            else:
                count -= 1
        return major


# @lc code=end
