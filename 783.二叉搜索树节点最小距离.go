/*
 * @lc app=leetcode.cn id=783 lang=golang
 *
 * [783] 二叉搜索树节点最小距离
 */

// @lc code=start
package main

import (
	"math"
)

// Definition for a binary tree node.
// type TreeNode struct {
// Val   int
// Left  *TreeNode
// Right *TreeNode
// }

const MaxDiff int = 100000

func minDiffInBST(root *TreeNode) int {
	if root != nil {
		leftMinDiff := minDiffInBST(root.Left)
		rightMinDiff := minDiffInBST(root.Right)
		left := root.Left
		leftDiff := MaxDiff
		if left != nil {
			for left != nil && left.Right != nil {
				left = left.Right
			}
			leftDiff = root.Val - left.Val
		}
		right := root.Right
		rightDiff := MaxDiff
		if right != nil {
			for right != nil && right.Left != nil {
				right = right.Left
			}
			rightDiff = right.Val - root.Val
		}
		return int(math.Min(math.Min(float64(leftDiff), float64(rightDiff)), math.Min(float64(leftMinDiff), float64(rightMinDiff))))

	} else {
		return MaxDiff
	}
}

// @lc code=end
