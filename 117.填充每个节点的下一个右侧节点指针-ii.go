/*
 * @lc app=leetcode.cn id=117 lang=golang
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */
// package main
//
// type Node struct {
// Val   int
// Left  *Node
// Right *Node
// Next  *Node
// }

func connect_(nodes []*Node) {
	for index := 0; index < len(nodes)-1; index++ {
		nodes[index].Next = nodes[index+1]
	}
}

func connect(root *Node) *Node {
	nodes := []*Node{}
	if root != nil {
		nodes = append(nodes, root)
	}
	for len(nodes) > 0 {
		connect_(nodes)
		new_nodes := []*Node{}
		for _, node := range nodes {
			if node.Left != nil {
				new_nodes = append(new_nodes, node.Left)
			}
			if node.Right != nil {
				new_nodes = append(new_nodes, node.Right)
			}
		}
		nodes = new_nodes
	}
	return root
}

// @lc code=end
