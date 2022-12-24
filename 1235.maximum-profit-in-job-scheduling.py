#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
from collections import defaultdict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startTime, endTime, profit = zip(
            *sorted(zip(startTime, endTime, profit)))
        dp: List[int] = [0] * len(profit)
        dp[-1] = profit[-1]

        for i in range(len(profit)-2, -1, -1):
            # Case 1: Exclude this job
            cur: int = dp[i+1]
            # Case 2: Include this job
            idx = self.binarySearch(startTime, endTime[i])
            if (idx == -1):
                cur = max(cur, profit[i])
            else:
                cur = max(cur, profit[i] + dp[idx])

            dp[i] = cur  # Memorize

        return dp[0]

    def binarySearch(self, arr: List[int], target: int):
        lp: int = 0
        rp: int = len(arr)-1
        rtn: int = -1

        while (lp <= rp):
            mp: int = lp + (rp - lp) // 2
            if (arr[mp] >= target):
                rtn = mp
                rp = mp - 1
            else:
                lp = mp + 1

        return rtn
# @lc code=end
