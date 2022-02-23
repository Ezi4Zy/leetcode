/*
 * @lc app=leetcode.cn id=173 lang=golang
 *
 * [173] 二叉搜索树迭代器
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
type BSTIterator struct {
	Nodes []*TreeNode
	Index int
}

func Constructor(root *TreeNode) BSTIterator {
	iterator := BSTIterator{}
	if root != nil {
		iterator.Nodes = append(iterator.Nodes, Constructor(root.Left).Nodes...)
		iterator.Nodes = append(iterator.Nodes, root)
		iterator.Nodes = append(iterator.Nodes, Constructor(root.Right).Nodes...)
	}
	return iterator
}

func (this *BSTIterator) Next() int {
	val := this.Nodes[this.Index].Val
	this.Index++
	return val

}

func (this *BSTIterator) HasNext() bool {
	return this.Index != len(this.Nodes)
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
// @lc code=end
