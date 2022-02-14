/*
 * @lc app=leetcode.cn id=872 lang=golang
 *
 * [872] 叶子相似的树
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

func getLeaves(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Left == nil && root.Right == nil {
		return []int{root.Val}
	}
	ret := []int{}
	ret = append(ret, getLeaves(root.Left)...)
	ret = append(ret, getLeaves(root.Right)...)
	return ret
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leaves1 := getLeaves(root1)
	leaves2 := getLeaves(root2)
	if len(leaves1) != len(leaves2) {
		return false
	}
	for i := 0; i < len(leaves1); i++ {
		if leaves1[i] != leaves2[i] {
			return false
		}
	}
	return true
}

// @lc code=end
