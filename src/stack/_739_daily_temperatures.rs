/*
 * @lc app=leetcode id=739 lang=rust
 *
 * [739] Daily Temperatures
 *
 * https://leetcode.com/problems/daily-temperatures/description/
 *
 * algorithms
 * Medium (66.09%)
 * Likes:    11207
 * Dislikes: 246
 * Total Accepted:    654K
 * Total Submissions: 989.7K
 * Testcase Example:  '[73,74,75,71,69,72,76,73]'
 *
 * Given an array of integers temperatures represents the daily temperatures,
 * return an array answer such that answer[i] is the number of days you have to
 * wait after the i^th day to get a warmer temperature. If there is no future
 * day for which this is possible, keep answer[i] == 0 instead.
 *
 *
 * Example 1:
 * Input: temperatures = [73,74,75,71,69,72,76,73]
 * Output: [1,1,4,2,1,1,0,0]
 * Example 2:
 * Input: temperatures = [30,40,50,60]
 * Output: [1,1,1,0]
 * Example 3:
 * Input: temperatures = [30,60,90]
 * Output: [1,1,0]
 *
 *
 * Constraints:
 *
 *
 * 1 <= temperatures.length <= 10^5
 * 30 <= temperatures[i] <= 100
 *
 *
 */
struct Solution;

// @lc code=start

use std::collections::VecDeque;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let len_ts: usize = temperatures.len();
        let mut stack: VecDeque<usize> = VecDeque::with_capacity(len_ts);
        let mut ans: Vec<i32> = vec![0; len_ts];

        for (idx, &num) in temperatures.iter().enumerate() {
            while let Some(&prev_idx) = stack.back() {
                if temperatures[prev_idx] < num {
                    ans[prev_idx] = (idx - prev_idx) as i32;
                    stack.pop_back();
                } else {
                    break;
                }
            }
            stack.push_back(idx);
        }

        ans
    }
}
// @lc code=end
