import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=46 lang=java
 *
 * [46] Permutations
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> perms = new ArrayList<>();
        dfs(perms, new ArrayList(), nums);
        return perms;
    }

    public void dfs(List<List<Integer>> rtn, ArrayList<Integer> arr, int[] targets) {
        if (arr.size() == targets.length) {
            rtn.add(new ArrayList<Integer>(arr));
        } else {
            for (int i : targets) {
                if (arr.contains(i)) {
                    continue;
                }
                arr.add(i);
                dfs(rtn, arr, targets);
                arr.remove(arr.size() - 1);
            }
        }
    }
}
// @lc code=end
