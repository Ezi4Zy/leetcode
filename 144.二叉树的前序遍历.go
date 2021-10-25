/*
 * @lc app=leetcode.cn id=144 lang=golang
 *
 * [144] 二叉树的前序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main


func preorderTraversal(root *TreeNode) []int {
	ret := []int{}
	if root != nil {
		ret = append(ret, root.Val)
		ret = append(ret, preorderTraversal(root.Left)...)
		ret = append(ret, preorderTraversal(root.Right)...)
	}
	return ret

}

// @lc code=end
