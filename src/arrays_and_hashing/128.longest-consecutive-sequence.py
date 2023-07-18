#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.87%)
# Likes:    17125
# Dislikes: 737
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        rtn = 0
        for n in nums:
            longest = 0
            if (n - 1) not in nums:
                base = n
                while base in nums:
                    base += 1
                rtn = max(rtn, base - n)

        return rtn


# @lc code=end
