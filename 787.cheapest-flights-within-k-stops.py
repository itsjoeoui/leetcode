#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        track = [inf] * n
        track[src] = 0

        for _ in range(k+1):
            tmp = track[:]
            for s, d, c in flights:
                tmp[d] = min(tmp[d], track[s] + c)
            track = tmp
        return track[dst] if track[dst] != inf else -1


# @lc code=end
