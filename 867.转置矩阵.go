/*
 * @lc app=leetcode.cn id=867 lang=golang
 *
 * [867] 转置矩阵
 */
package main

// @lc code=start
func transpose(matrix [][]int) [][]int {
	if len(matrix) == len(matrix[0]) {
		for i := 0; i < len(matrix); i++ {
			for j := i + 1; j < len(matrix); j++ {
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			}
		}
		return matrix
	} else {
		ret := [][]int{}
		for i := 0; i < len(matrix[0]); i++ {
			row := []int{}
			for j := 0; j < len(matrix); j++ {
				row = append(row, matrix[j][i])
			}
			ret = append(ret, row)
		}
		return ret
	}
}

// func main() {
// fmt.Println(transpose([][]int{
// {1, 2, 3},
// {4, 5, 6},
// {7, 8, 9},
// }), transpose([][]int{
// {1, 2, 3},
// {4, 5, 6},
// }))
// }

// @lc code=end
