#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        total = 0

        for r_i in range(rows):
            for c_i in range(cols):
                total += grid[r_i][c_i] * 4

                if r_i > 0:
                    total -= grid[r_i][c_i] * grid[r_i-1][c_i]

                if r_i < rows-1:
                    total -= grid[r_i][c_i] * grid[r_i+1][c_i]

                if c_i > 0:
                    total -= grid[r_i][c_i] * grid[r_i][c_i-1]

                if c_i < cols-1:
                    total -= grid[r_i][c_i] * grid[r_i][c_i+1]

        return total
# @lc code=end
