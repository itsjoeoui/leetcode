/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (62.87%)
 * Likes:    9147
 * Dislikes: 286
 * Total Accepted:    2.2M
 * Total Submissions: 3.5M
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 *
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 5 * 10^4
 * s and t consist of lowercase English letters.
 *
 *
 *
 * Follow up: What if the inputs contain Unicode characters? How would you
 * adapt your solution to such a case?
 *
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut history = HashMap::new();
        for c in s.chars() {
            history.entry(c).and_modify(|e| *e += 1).or_insert(1);
        }
        for c in t.chars() {
            if let Some(e) = history.get_mut(&c) {
                *e -= 1;
                if *e == 0 {
                    history.remove(&c);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
