import java.util.ArrayList;

/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 */

// @lc code=start
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> rtn = new ArrayList<>();
        gen(rtn, new ArrayList<Integer>(), nums, 0);
        return rtn;
    }

    public void gen(List<List<Integer>> rtn, ArrayList<Integer> cur, int[] nums, int idx) {
        rtn.add(new ArrayList<Integer>(cur));
        for (int i = idx; i < nums.length; i++) {
            cur.add((Integer) nums[i]);
            gen(rtn, cur, nums, i + 1);
            cur.remove((Integer) nums[i]);
        }
    }
}
// @lc code=end
