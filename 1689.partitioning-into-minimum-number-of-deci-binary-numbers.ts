/*
 * @lc app=leetcode id=1689 lang=typescript
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
function minPartitions(n: string): number {
  var result: string = "0";

  for (let num of n) {
    if (num > result) {
      result = num;
    }
  }
  return Number(result);
}
// @lc code=end
