#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                lp, rp = 0, len(row)-1
                while lp <= rp:
                    mp = lp + (rp - lp) // 2
                    if row[mp] == target:
                        return True
                    elif row[mp] < target:
                        lp = mp + 1
                    else:
                        rp = mp - 1
        return False
    # A cool adaptive search approach
    # https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90+-w-Diagram

# @lc code=end
