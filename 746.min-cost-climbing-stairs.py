#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = cost[1], cost[0]

        for i in range(2, len(cost)):
            tmp = min(dp1, dp2) + cost[i]
            dp2, dp1 = dp1, tmp

        return min(dp1, dp2)

# @lc code=end
