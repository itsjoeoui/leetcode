#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track: defaultdict = defaultdict(lambda: 0)
        half = len(nums) // 2
        for n in nums:
            track[n] += 1
            if track[n] > half:
                return n
        return -1


# @lc code=end
