#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo: dict[int, int] = dict()
        for i in coins:
            memo[i] = 1
        memo[0] = 0

        def dfs(sum: int) -> int:
            if sum in memo:
                return memo[sum]
            if sum < 0:
                return inf

            count: int = min([dfs(sum - i) for i in coins])

            memo[sum] = count + 1
            return count + 1

        rtn: int = dfs(amount)
        return rtn if rtn != inf else -1


# @lc code=end
