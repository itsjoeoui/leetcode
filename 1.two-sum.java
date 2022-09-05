/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // int[] result = new int[2];
        HashMap<Integer, Integer> history = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (history.containsKey(target - nums[i])) {
                // result[0] = i;
                // result[1] = history.get(target-nums[i]);
                // return result;
                return new int[] { i, history.get(target - nums[i]) };
            }
            history.put(nums[i], i);
        }
        return new int[] { 0, 0 };
    }
}
// @lc code=end
