/*
 * @lc app=leetcode id=589 lang=golang
 *
 * [589] N-ary Tree Preorder Traversal
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func preorder(root *Node) []int {
	if root == nil {
		return []int{}
	}
	stack, ans := []*Node{root}, []int{}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:(len(stack) - 1)]
		ans = append(ans, pop.Val)
		for i := len(pop.Children) - 1; i >= 0; i-- {
			stack = append(stack, pop.Children[i])
		}
	}
	return ans
}

// @lc code=end

