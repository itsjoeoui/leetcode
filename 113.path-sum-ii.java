/*
 * @lc app=leetcode id=113 lang=java
 *
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (56.82%)
 * Likes:    6599
 * Dislikes: 135
 * Total Accepted:    713.5K
 * Total Submissions: 1.3M
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given the root of a binary tree and an integer targetSum, return all
 * root-to-leaf paths where the sum of the node values in the path equals
 * targetSum. Each path should be returned as a list of the node values, not
 * node references.
 * 
 * A root-to-leaf path is a path starting from the root and ending at any leaf
 * node. A leaf is a node with no children.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
 * Output: [[5,4,11,2],[5,8,4,5]]
 * Explanation: There are two paths whose sum equals targetSum:
 * 5 + 4 + 11 + 2 = 22
 * 5 + 8 + 4 + 5 = 22
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,2,3], targetSum = 5
 * Output: []
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root = [1,2], targetSum = 0
 * Output: []
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 5000].
 * -1000 <= Node.val <= 1000
 * -1000 <= targetSum <= 1000
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> curPath = new ArrayList();
        List<List<Integer>> allPath = new ArrayList();

        dfs(root, curPath, allPath, targetSum, 0);

        return allPath;
    }

    public void dfs(TreeNode root, List<Integer> curPath, List<List<Integer>> allPath, int targetSum, int curSum) {
        if (root == null) {
            return;
        }

        curSum += root.val;
        curPath.add(root.val);

        if (root.left == null && root.right == null) {
            if (targetSum == curSum) {
                allPath.add(new ArrayList<Integer>(curPath));
            }
        } else {
            dfs(root.left, curPath, allPath, targetSum, curSum);
            dfs(root.right, curPath, allPath, targetSum, curSum);
        }

        curPath.remove(curPath.size() - 1);
        curSum -= root.val;
    }
}
// @lc code=end
