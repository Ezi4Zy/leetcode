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
	vals []*TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
	iterator := BSTIterator{}
	iterator.inorder(root)
	return iterator
}

func (this *BSTIterator) inorder(root *TreeNode) {
	if root == nil {
		return
	}
	this.inorder(root.Left)
	this.vals = append(this.vals, root)
	this.inorder(root.Right)

}

func (this *BSTIterator) Next() int {
	val := this.vals[0].Val
	this.vals = this.vals[1:]
	return val
}

func (this *BSTIterator) HasNext() bool {
	return len(this.vals) != 0
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
// @lc code=end
