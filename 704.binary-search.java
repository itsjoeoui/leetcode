/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        int lp = 0;
        int rp = nums.length - 1;

        while (lp <= rp) {
            int mp = lp + (rp - lp) / 2;
            if (nums[mp] == target) {
                return mp;
            }
            if (nums[mp] < target) {
                lp = mp + 1;
            } else {
                rp = mp - 1;
            }
        }
        return -1;
    }
}
// @lc code=end
