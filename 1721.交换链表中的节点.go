/*
 * @lc app=leetcode.cn id=1721 lang=golang
 *
 * [1721] 交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// package leetcode
//
// type ListNode struct {
// Val  int
// Next *ListNode
// }

func swapNodes(head *ListNode, k int) *ListNode {
	node1 := head
	for i := 1; i < k; i++ {
		node1 = node1.Next
	}
	node2 := node1
	node3 := head
	for node2.Next != nil {
		node2 = node2.Next
		node3 = node3.Next
	}
	node1.Val, node3.Val = node3.Val, node1.Val
	return head
}

// @lc code=end
