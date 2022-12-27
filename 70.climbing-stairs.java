/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();

    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        if (this.memo.containsKey(n)) {
            return this.memo.get(n);
        }

        this.memo.put(n, (climbStairs(n-1)+ climbStairs(n-2)));
        return this.memo.get(n);
    }
}
// @lc code=end
