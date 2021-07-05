/*
 * @lc app=leetcode.cn id=1080 lang=golang
 *
 * [1080] 根到叶路径上的不足节点
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

//  package main
// 
//  type TreeNode struct {
	//  Val int
	//  Left *TreeNode
	//  Right *TreeNode
//  }

func sufficientSubset(root *TreeNode, limit int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Left == nil && root.Right == nil{
		if root.Val < limit{
			return nil
		}else{
			return root
		}
	}
	root.Left = sufficientSubset(root.Left, limit - root.Val)
	root.Right = sufficientSubset(root.Right, limit - root.Val)
	if root.Left == nil && root.Right == nil{
		return nil
	}
	return root
}
// @lc code=end

