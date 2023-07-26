#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (66.09%)
# Likes:    11207
# Dislikes: 246
# Total Accepted:    654K
# Total Submissions: 989.7K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#

from collections import deque
from typing import List

# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rtn = [0] * len(temperatures)
        stack = deque([0])

        for i in range(1, len(temperatures)):
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                rtn[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return rtn


# @lc code=end
