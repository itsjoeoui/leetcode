#
# @lc app=leetcode id=2055 lang=python3
#
# [2055] Plates Between Candles
#

# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == "|"]
        output = []

        for s, e in queries:
            l, r = 0, len(candles)-1
            l_candle = -1
            while l <= r:
                m = l + (r-l)//2
                if candles[m] >= s:
                    l_candle = m
                    r = m - 1
                else:
                    l = m + 1

            l, r = 0, len(candles)-1
            r_candle = -1
            while l <= r:
                m = l + (r-l)//2
                if candles[m] <= e:
                    r_candle = m
                    l = m + 1
                else:
                    r = m - 1

            if l_candle >= r_candle or candles[l_candle] >= e or candles[r_candle] <= s:
                output.append(0)
            else:
                output.append(
                    candles[r_candle] - candles[l_candle] + 1 - (r_candle - l_candle+1))

        return output

# @lc code=end
