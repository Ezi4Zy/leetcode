/*
 * @lc app=leetcode.cn id=993 lang=golang
 *
 * [993] 二叉树的堂兄弟节点
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

func getDeepthAndFather(root *TreeNode, val int) (int, *TreeNode) {
	if root.Left != nil {
		if root.Left.Val == val {
			return 1, root
		} else {
			deepth, father := getDeepthAndFather(root.Left, val)
			if father != nil {
				return deepth + 1, father
			}
		}
	}
	if root.Right != nil {
		if root.Right.Val == val {
			return 1, root
		} else {
			deepth, father := getDeepthAndFather(root.Right, val)
			if father != nil {
				return deepth + 1, father
			}
		}
	}
	return -1, nil
}

func isCousins(root *TreeNode, x int, y int) bool {
	if root.Val == x || root.Val == y {
		return false
	}
	xDeepth, xFather := getDeepthAndFather(root, x)
	yDeepth, yFather := getDeepthAndFather(root, y)
	return xDeepth == yDeepth && xFather != yFather

}

// @lc code=end
