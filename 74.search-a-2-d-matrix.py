#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r_max, c_max = len(matrix)-1, len(matrix[0])-1
        r_cur, c_cur = r_max, 0
        while True:
            tmp = matrix[r_cur][c_cur]
            if target == tmp:
                return True
            if tmp < target:
                c_cur += 1
                if c_cur > c_max:
                    return False
            else:
                r_cur -= 1
                if r_cur < 0:
                    return False

# @lc code=end
