/*
 * @lc app=leetcode id=90 lang=java
 *
 * [90] Subsets II
 */

// @lc code=start
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> rtn = new ArrayList<>();
        Arrays.sort(nums);
        gen(rtn, new ArrayList<Integer>(), nums, 0);
        return rtn;
    }

    public void gen(List<List<Integer>> rtn, ArrayList<Integer> cur, int[] nums, int idx) {
        rtn.add(new ArrayList<Integer>(cur));
        for (int i = idx; i < nums.length; i++) {
            if (i > idx && nums[i - 1] == nums[i])
                continue;
            cur.add((Integer) nums[i]);
            gen(rtn, cur, nums, i + 1);
            cur.remove((Integer) nums[i]);
        }
    }
}
// @lc code=end
