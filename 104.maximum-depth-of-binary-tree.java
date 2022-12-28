import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=104 lang=java
 *
 * [104] Maximum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Deque<TreeNode> node = new LinkedList<TreeNode>();
        Deque<Integer> depth = new LinkedList<Integer>();

        node.addLast(root);
        depth.addLast(1);

        int level = 1;

        while (!depth.isEmpty()) {
            TreeNode cn = node.removeFirst();
            Integer cd = depth.removeFirst();

            level = cd > level ? cd : level;

            if (cn.left != null) {
                node.addLast(cn.left);
                depth.addLast(cd + 1);
            }

            if (cn.right != null) {
                node.addLast(cn.right);
                depth.addLast(cd + 1);
            }

        }
        return level;
    }
}
// @lc code=end
