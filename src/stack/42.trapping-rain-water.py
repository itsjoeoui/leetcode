#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (58.98%)
# Likes:    26686
# Dislikes: 366
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # the idea is basically traversing the array twice
        # first time, we find the max height from left to right
        # second time, we find the max height from right to left
        # then we can calculate the water trapped at each index
        # and sum them up
        # time complexity: O(n)
        # space complexity: O(n)
        total = 0
        stack = deque()
        cm = 0
        length = len(height)
        for i in range(length):
            cm = max(height[i], cm)
            stack.append(cm)
        cm = 0
        for i in range(length - 1, -1, -1):
            cm = max(height[i], cm)
            ce = stack.pop()
            total += min(ce, cm) - height[i]
        return total


# @lc code=end
