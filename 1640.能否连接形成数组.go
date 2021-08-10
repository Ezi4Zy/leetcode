/*
 * @lc app=leetcode.cn id=1640 lang=golang
 *
 * [1640] 能否连接形成数组
 */

// @lc code=start
package main

func canFormArray(arr []int, pieces [][]int) bool {
	index := 0
	for index < len(arr) {
		cur := index
		for i := 0; i < len(pieces); i++ {
			if arr[index] == pieces[i][0] {
				j := 1
				index++
				for j < len(pieces[i]) && arr[index] == pieces[i][j] {
					index++
					j++
				}
				if j != len(pieces[i]) {
					return false
				} else {
					break
				}
			}
		}
		if cur == index {
			return false
		}
	}
	return true
}

// @lc code=end
