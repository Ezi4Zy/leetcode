/*
 * @lc app=leetcode.cn id=1791 lang=golang
 *
 * [1791] 找出星型图的中心节点
 */

// @lc code=start

func findCenter(edges [][]int) int {
	if edges[1][0] == edges[0][0] || edges[1][0] == edges[0][1] {
		return edges[1][0]
	} else {
		return edges[1][1]
	}
}

// @lc code=end

