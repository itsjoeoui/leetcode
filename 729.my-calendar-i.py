#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.timeline = []
        self.length = 0

    def book(self, start: int, end: int) -> bool:
        l, r, i = 0, self.length-1, self.length

        while l <= r:
            m = l + (r-l) // 2
            if self.timeline[m][0] > start:
                i = m
                r = m - 1
            else:
                l = m + 1

        if (i > 0 and self.timeline[i-1][1] > start) or (i < self.length and self.timeline[i][0] < end):
            return False

        self.timeline.insert(i, (start, end))
        self.length += 1
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
