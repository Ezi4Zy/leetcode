/*
 * @lc app=leetcode.cn id=445 lang=golang
 *
 * [445] 两数相加 II
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
// 
// type ListNode struct{
	// Val int
	// Next *ListNode
// }
func addTwoNumbers_(l1 *ListNode, l2 *ListNode) (int, *ListNode){
	if l1 != nil && l2 != nil{
		num, node := addTwoNumbers_(l1.Next, l2.Next)
		l1.Next = node
		val := num + l1.Val + l2.Val
		l1.Val = val % 10
		return val / 10, l1
	}
	return 0, nil

}
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head1 := l1
	head2 := l2
	len1 := 0
	len2 := 0
	for l1 != nil{
		len1 += 1
		l1 = l1.Next
	}
	for l2 != nil{
		len2 += 1
		l2 = l2.Next
	}
	if len1 >= len2{
		diff := len1 - len2
		for diff > 0{
			diff -= 1
			node := &ListNode{
				Val: 0,
				Next: head2,
			}
			head2 = node
		}
	}else {
		diff := len2 - len1
		for diff > 0{
			diff -= 1
			node := &ListNode{
				Val: 0,
				Next: head1,
			}
			head1 = node
		}
	}
	num, head := addTwoNumbers_(head1, head2)
	if num != 0{
		node := &ListNode{
			Val: num,
			Next: head,
		}
		return node
	}
	return head
}
// @lc code=end

