package leetcode

/*
 * @lc app=leetcode id=142 lang=golang
 *
 * [142] Linked List Cycle II
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	// Floyd's cycle detection algorithm
	s, f := head, head
	for f != nil && f.Next != nil {
		s, f = s.Next, f.Next.Next
		if s == f {
			for s != head {
				s, head = s.Next, head.Next
			}
			return s
		}
	}
	return nil

}

// @lc code=end
