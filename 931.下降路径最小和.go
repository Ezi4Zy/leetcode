/*
 * @lc app=leetcode.cn id=931 lang=golang
 *
 * [931] 下降路径最小和
 */
package main

// @lc code=start
func minFallingPathSum(matrix [][]int) int {
	for i := len(matrix) - 2; i >= 0; i-- {
		for j := 0; j < len(matrix[0]); j++ {
			tmp1, tmp2, tmp3 := 100*len(matrix), matrix[i+1][j], 100*len(matrix)
			if j > 0 {
				tmp1 = matrix[i+1][j-1]
			}
			if j < len(matrix[0])-1 {
				tmp3 = matrix[i+1][j+1]
			}
			if tmp1 > tmp2 {
				if tmp2 > tmp3 {
					matrix[i][j] += tmp3
				} else {
					matrix[i][j] += tmp2
				}
			} else {
				if tmp1 > tmp3 {
					matrix[i][j] += tmp3
				} else {
					matrix[i][j] += tmp1
				}
			}
		}
	}
	count := matrix[0][0]
	for i := 1; i < len(matrix[0]); i++ {
		if matrix[0][i] < count {
			count = matrix[0][i]
		}
	}
	return count
}

// func main() {
// fmt.Println(minFallingPathSum([][]int{
// {2, 1, 3},
// {6, 5, 4},
// {7, 8, 9},
// }))
// fmt.Println(minFallingPathSum([][]int{
// {-19, 57},
// {-40, -5},
// }))
// }

// @lc code=end
