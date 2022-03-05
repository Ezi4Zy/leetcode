/*
 * @lc app=leetcode.cn id=701 lang=golang
 *
 * [701] 二叉搜索树中的插入操作
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

func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{
			Val: val,
		}
	} else {
		if root.Val > val {
			root.Left = insertIntoBST(root.Left, val)

		} else {
			root.Right = insertIntoBST(root.Right, val)
		}
		return root
	}
}

// func main() {
// root := &TreeNode{
// Val: 7,
// }
// root = insertIntoBST(root, 5)
// fmt.Println(root, root.Left, root.Right)

// }

// @lc code=end
