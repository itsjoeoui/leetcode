#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        color_before = image[sr][sc]

        if color_before == color:
            return image

        r_len, c_len = len(image), len(image[0])

        queue = deque([(sr, sc)])

        while queue:
            nr, nc = queue.popleft()
            image[nr][nc] = color
            for r, c in ((nr+1, nc), (nr-1, nc), (nr, nc+1), (nr, nc-1)):
                if 0 <= r < r_len and 0 <= c < c_len:
                    if image[r][c] == color_before:
                        queue.append((r, c))

        return image
# @lc code=end
