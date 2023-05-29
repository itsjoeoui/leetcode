import java.util.HashSet;

/*
 * @lc app=leetcode id=217 lang=java
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int n : nums) {
            if (!hs.add(n)) {
                return true;
            }
        }
        return false;
    }
}
// @lc code=end
