#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque

        queue, total = deque([n]), 0
        seen = [0 for i in range(n)]

        while queue:
            total += 1
            level = len(queue)

            for _ in range(level):
                cur = queue.popleft()

                for i in range(1, int(math.sqrt(cur) + 1)):
                    temp = cur-i*i

                    if seen[temp] == 0:

                        next = cur-i*i

                        if next == 0:
                            return total

                        queue.append(next)
                        seen[next] = 1

# @lc code=end
