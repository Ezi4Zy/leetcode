/*
 * @lc app=leetcode.cn id=1380 lang=golang
 *
 * [1380] 矩阵中的幸运数
 */

// @lc code=start
package main

func luckyNumbers(matrix [][]int) []int {
	ret := []int{}
	for minRow := 0; minRow < len(matrix); minRow++ {
		minCol := 0
		for i := 1; i < len(matrix[0]); i++ {
			if matrix[minRow][i] < matrix[minRow][minCol] {
				minCol = i
			}
		}
		flag := true
		for i := 0; i < len(matrix); i++ {
			if matrix[i][minCol] > matrix[minRow][minCol] {
				flag = false
				break
			}
		}
		if flag {
			ret = append(ret, matrix[minRow][minCol])
		}

	}
	return ret
}

// @lc code=end
