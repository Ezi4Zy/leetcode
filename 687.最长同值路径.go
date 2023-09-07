/*
 * @lc app=leetcode.cn id=687 lang=golang
 *
 * [687] 最长同值路径
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
// type TreeNode struct {
// Val   int
// Left  *TreeNode
// Right *TreeNode
// }

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func longestUnivaluePath(root *TreeNode) int {
	var dfs func(*TreeNode) int
	var ans int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		left1, right1 := 0, 0
		if node.Left != nil && node.Left.Val == node.Val {
			left1 = left + 1
		}
		if node.Right != nil && node.Right.Val == node.Val {
			right1 = right + 1
		}
		ans = max(ans, left1+right1)
		return max(left1, right1)
	}
	dfs(root)
	return ans

}

// @lc code=end

