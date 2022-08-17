#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # I realize later that I don't actually need to simulate every single move
        # I could have used a for loop to append the most outside col/row
        # But too late, already wrote the simulation here and I am too lazy to change

        # Time: O(n)
        row_move, col_move = 0, 1

        cur_row, cur_col = 0, 0

        row_upper, col_upper = len(matrix), len(matrix[0])
        row_lower, col_lower = 0, 0

        output = []

        for _ in range(row_upper*col_upper):
            output.append(matrix[cur_row][cur_col])

            next_row, next_col = cur_row + row_move, cur_col + col_move

            if next_row >= row_upper:
                row_move, col_move = 0, -1
                next_row, next_col = next_row - 1, next_col - 1
                col_upper -= 1

            elif next_row < row_lower:
                row_move, col_move = 0, 1
                next_row, next_col = next_row + 1, next_col + 1
                col_lower += 1

            elif next_col >= col_upper:
                row_move, col_move = 1, 0
                next_row, next_col = next_row + 1, next_col - 1
                row_lower += 1

            elif next_col < col_lower:
                row_move, col_move = -1, 0
                next_row, next_col = next_row - 1, next_col + 1
                row_upper -= 1

            cur_row, cur_col = next_row, next_col

        return output
# @lc code=end
