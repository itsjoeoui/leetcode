/*
 * @lc app=leetcode id=22 lang=rust
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (73.05%)
 * Likes:    18844
 * Dislikes: 758
 * Total Accepted:    1.5M
 * Total Submissions: 2M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 *
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 8
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut rtn: Vec<String> = Vec::new();

        fn dfs(left: i32, right: i32, current: String, n: i32, rtn: &mut Vec<String>) {
            if right == n {
                rtn.push(current);
                return;
            }
            if left > right {
                dfs(left, right + 1, current.to_owned() + ")", n, rtn)
            }
            if left < n {
                dfs(left + 1, right, current.to_owned() + "(", n, rtn)
            }
        }

        dfs(1, 0, "(".into(), n, &mut rtn);

        rtn
    }
}
// @lc code=end
