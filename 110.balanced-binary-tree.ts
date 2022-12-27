/*
 * @lc app=leetcode id=110 lang=typescript
 *
 * [110] Balanced Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isBalanced(root: TreeNode | null): boolean {
  let rtn: number = depth(root);
  return rtn == -1 ? false : true;
}

function depth(root: TreeNode | null): number {
  if (root === null) {
    return 0;
  }

  let left: number = depth(root.left);
  if (left == -1) {
    return -1;
  }
  let right: number = depth(root.right);
  if (right == -1) {
    return -1;
  }
  if (Math.abs(left - right) > 1) {
    return -1;
  }
  return Math.max(left, right) + 1;
}
// @lc code=end
