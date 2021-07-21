/*
 * @lc app=leetcode.cn id=92 lang=golang
 *
 * [92] 反转链表 II
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

func reverse(node *ListNode, next *ListNode) *ListNode {
	if node == nil {
		return nil
	}
	nodeNext := node.Next
	if nodeNext == nil {
		node.Next = next
		return node
	} else {
		node.Next = next
		return reverse(nodeNext, node)
	}

}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	head = &ListNode{Next: head}
	leftPreNode := head
	for left > 1 {
		leftPreNode = leftPreNode.Next
		left--
	}
	rightNextNode := head
	for right > 0 {
		rightNextNode = rightNextNode.Next
		right--
	}
	rightNextNode, rightNextNode.Next = rightNextNode.Next, nil
	leftPreNode.Next = reverse(leftPreNode.Next, rightNextNode)
	return head.Next
}

// @lc code=end
