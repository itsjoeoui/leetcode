import java.util.Arrays;
import java.util.Iterator;
import java.util.StringJoiner;

/*
 * @lc app=leetcode id=297 lang=java
 *
 * [297] Serialize and Deserialize Binary Tree
 *
 * https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
 *
 * algorithms
 * Hard (55.16%)
 * Likes:    8245
 * Dislikes: 300
 * Total Accepted:    710.1K
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,2,3,null,null,4,5]'
 *
 * Serialization is the process of converting a data structure or object into a
 * sequence of bits so that it can be stored in a file or memory buffer, or
 * transmitted across a network connection link to be reconstructed later in
 * the same or another computer environment.
 * 
 * Design an algorithm to serialize and deserialize a binary tree. There is no
 * restriction on how your serialization/deserialization algorithm should work.
 * You just need to ensure that a binary tree can be serialized to a string and
 * this string can be deserialized to the original tree structure.
 * 
 * Clarification: The input/output format is the same as how LeetCode
 * serializes a binary tree. You do not necessarily need to follow this format,
 * so please be creative and come up with different approaches yourself.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [1,2,3,null,null,4,5]
 * Output: [1,2,3,null,null,4,5]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = []
 * Output: []
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 10^4].
 * -1000 <= Node.val <= 1000
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
 * TreeNode(int x) { val = x; }
 * }
 */
import java.util.StringJoiner;

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringJoiner result = new StringJoiner(" ");
        serializeDFS(root, result);
        return result.toString();
    }

    public void serializeDFS(TreeNode root, StringJoiner result) {
        if (root == null) {
            result.add("x");
            return;
        }
        result.add(Integer.toString(root.val));
        serializeDFS(root.left, result);
        serializeDFS(root.right, result);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        return deserializeDFS(Arrays.stream(data.split(" ")).iterator());
    }

    public TreeNode deserializeDFS(Iterator<String> nodes) {
        String val = nodes.next();
        if (val.equals("x")) {
            return null;
        }
        TreeNode cur = new TreeNode(Integer.parseInt(val));
        cur.left = deserializeDFS(nodes);
        cur.right = deserializeDFS(nodes);

        return cur;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// @lc code=end
