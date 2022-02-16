/*
 * @lc app=leetcode.cn id=1022 lang=golang
 *
 * [1022] 从根到叶的二进制数之和
 */
package main

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// type TreeNode struct {
// Val   int
// Left  *TreeNode
// Right *TreeNode
// }

func sumNodeToLeft(val int, node *TreeNode) int {
	if node != nil {
		if node.Left != nil || node.Right != nil {
			total := 0
			if node.Left != nil {
				total += sumNodeToLeft(val*2+node.Val, node.Left)
			}
			if node.Right != nil {
				total += sumNodeToLeft(val*2+node.Val, node.Right)
			}
			return total
		} else {
			return val*2 + node.Val
		}
	}
	return val
}

func sumRootToLeaf(root *TreeNode) int {
	return sumNodeToLeft(0, root)
}

// @lc code=end
