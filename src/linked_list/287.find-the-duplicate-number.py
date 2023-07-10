#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (59.12%)
# Likes:    19861
# Dislikes: 3079
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
#
#
# Example 1:
#
#
# Input: nums = [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: nums = [3,1,3,4,2]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
#
#
#
# Follow up:
#
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection algorithm
        # Classic slow and fast pointer
        # Just gotta remember this one

        sp, fp = nums[nums[0]], nums[nums[nums[0]]]
        while sp != fp:
            sp = nums[sp]
            fp = nums[nums[fp]]

        sp = nums[0]
        while sp != fp:
            sp = nums[sp]
            fp = nums[fp]
        return sp


# @lc code=end
