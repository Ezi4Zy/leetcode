/*
 * @lc app=leetcode.cn id=2022 lang=golang
 *
 * [2022] 将一维数组转变成二维数组
 */

package main

import "fmt"

// @lc code=start
func construct2DArray(original []int, m int, n int) [][]int {
	if len(original) != m*n {
		return [][]int{}
	}
	ret := make([][]int, m)
	for i := 0; i < m; i++ {
		ret[i] = make([]int, n)
		for j := 0; j < n; j++ {
			ret[i][j] = original[i*n+j]
		}
	}
	return ret
}

// @lc code=end

func main() {
	fmt.Println(construct2DArray([]int{1, 2, 3, 4}, 2, 2))
	fmt.Println(construct2DArray([]int{1, 2, 3}, 1, 3))
	fmt.Println(construct2DArray([]int{1, 2}, 1, 1))
	fmt.Println(construct2DArray([]int{3}, 1, 2))
}
