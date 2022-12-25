#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        r_num = len(mat)
        c_num = len(mat[0])

        for r in range(r_num):
            for c in range(c_num):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(r_num-1, -1, -1):
            for c in range(c_num-1, -1, -1):
                if mat[r][c] > 0:
                    bot = mat[r+1][c] if r < r_num - 1 else math.inf
                    right = mat[r][c+1] if c < c_num - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bot+1, right+1)

        return mat
# @lc code=end
