/*
 * @lc app=leetcode.cn id=938 lang=golang
 *
 * [938] 二叉搜索树的范围和
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
func rangeSumBST(root *TreeNode, low int, high int) int {
	if root != nil {
		if root.Val >= low && root.Val <= high {
			return root.Val + rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
		} else {
			return rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
		}

	}
	return 0
}

// @lc code=end

