#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m_len, n_len = len(grid), len(grid[0])

        counter = 0

        def dfs(m, n):
            grid[m][n] = "X"
            for nm, nn in ((m+1, n), (m-1, n), (m, n+1), (m, n-1)):
                if 0 <= nm < m_len and 0 <= nn < n_len:
                    if grid[nm][nn] == "1":
                        dfs(nm, nn)

        for m in range(m_len):
            for n in range(n_len):
                if grid[m][n] == '1':
                    counter += 1
                    dfs(m, n)

        return counter
# @lc code=end
