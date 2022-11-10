#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:

    def __init__(self, length: int):
        self.sid = - 1
        self.history = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.sid, val])

    def snap(self) -> int:
        self.sid += 1
        return self.sid

    def get(self, index: int, snap_id: int) -> int:
        l, r = 0, len(self.history[index])-1
        rtn = -1
        while l <= r:
            m = l + (r-l) // 2
            if self.history[index][m][0] < snap_id:
                rtn = m
                l = m + 1
            else:
                r = m - 1
        return self.history[index][rtn][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end
