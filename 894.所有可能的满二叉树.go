/*
 * @lc app=leetcode.cn id=894 lang=golang
 *
 * [894] 所有可能的满二叉树
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
// package main
//
// type TreeNode struct {
// Val   int
// Left  *TreeNode
// Right *TreeNode
// }

var AllPossibleFBTs map[int][]*TreeNode

func allPossibleFBT_(n int) []*TreeNode {
	_, ok := AllPossibleFBTs[n]
	if !ok {
		tmp := []*TreeNode{}
		for i := 0; i < n; i++ {
			j := n - i - 1
			for _, left := range allPossibleFBT_(i) {
				for _, right := range allPossibleFBT_(j) {
					tmp = append(tmp, &TreeNode{
						Val:   0,
						Left:  left,
						Right: right,
					})
				}
			}
		}
		AllPossibleFBTs[n] = tmp
	}

	return AllPossibleFBTs[n]
}

func allPossibleFBT(n int) []*TreeNode {
	AllPossibleFBTs = make(map[int][]*TreeNode)
	AllPossibleFBTs[0] = []*TreeNode{}
	AllPossibleFBTs[1] = append(AllPossibleFBTs[1], &TreeNode{Val: 0})
	return allPossibleFBT_(n)

}

// @lc code=end
