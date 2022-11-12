#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.kvstore = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        target = self.kvstore[key]
        l, r, idx = 0, len(target)-1, len(target)
        while l <= r:
            m = l + (r - l) // 2
            if target[m][0] >= timestamp:
                idx = m
                r = m - 1
            else:
                l = m + 1
        if idx < len(target):
            if target[idx][0] == timestamp:
                target[idx][1] = value
            else:
                target.insert(idx, [timestamp, value])
        else:
            target.append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        target = self.kvstore[key]
        l, r, idx = 0, len(target)-1, len(target)
        while l <= r:
            m = l + (r - l) // 2
            if target[m][0] <= timestamp:
                idx = m
                l = m + 1
            else:
                r = m - 1
        if idx < len(target):
            return target[idx][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
