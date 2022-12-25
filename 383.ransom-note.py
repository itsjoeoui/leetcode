#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ht = defaultdict(lambda: 0)

        for i in range(len(ransomNote)):
            ht[ransomNote[i]] -= 1

        for i in range(len(magazine)):
            ht[magazine[i]] += 1

        for v in ht.values():
            if v < 0:
                return False
        return True


# @lc code=end
