/*
 * @lc app=leetcode id=33 lang=typescript
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
function search(nums: number[], target: number): number {
  let lp: number = 0;
  let rp: number = nums.length - 1;

  while (lp <= rp) {
    let mp: number = Math.floor(lp + (rp - lp) / 2);
    console.log(mp);
    if (nums[mp] == target) {
      return mp;
    }
    if (nums[mp] <= nums[nums.length - 1]) {
      if (target > nums[nums.length - 1]) {
        rp = mp - 1;
      } else {
        if (nums[mp] < target) {
          lp = mp + 1;
        } else {
          rp = mp - 1;
        }
      }
    } else {
      if (target <= nums[nums.length - 1]) {
        lp = mp + 1;
      } else {
        if (nums[mp] < target) {
          lp = mp + 1;
        } else {
          rp = mp - 1;
        }
      }
    }
  }
  return -1;
}
// @lc code=end
