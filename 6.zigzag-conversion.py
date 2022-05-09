#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s  # Return itself since 1 row means nothing changed

        levelList = [""] * numRows  # Each index represents one level

        currentLevel = 0
        step = 1

        for v in s:
            levelList[currentLevel] += v

            if currentLevel == 0:
                step = 1
            elif currentLevel == numRows-1:
                step = -1

            currentLevel += step

        return "".join(levelList)
# @lc code=end
