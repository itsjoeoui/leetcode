#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, target_idx, seen):

            if board[row][col] == word[target_idx]:
                if (row, col) in seen:
                    return False
                if target_idx == len(word) - 1:
                    return True

                if row > 0:
                    if dfs(row-1, col, target_idx+1, seen+deque([(row, col)])):
                        return True
                if row < len(board)-1:
                    if dfs(row+1, col, target_idx+1,  seen+deque([(row, col)])):
                        return True
                if col > 0:
                    if dfs(row, col-1, target_idx+1,  seen+deque([(row, col)])):
                        return True
                if col < len(board[0])-1:
                    if dfs(row, col+1, target_idx+1,  seen+deque([(row, col)])):
                        return True

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, deque([])):
                        return True
        return False

# @lc code=end
