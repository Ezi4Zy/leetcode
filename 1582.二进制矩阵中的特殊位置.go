/*
 * @lc app=leetcode.cn id=1582 lang=golang
 *
 * [1582] 二进制矩阵中的特殊位置
 */

// @lc code=start

package main

func numSpecial(mat [][]int) int {
	rowLength := len(mat)
	colLength := len(mat[0])
	rows := make([]int, rowLength)
	cols := make([]int, colLength)
	count := 0
	for i := 0; i < rowLength; i++ {
		for j := 0; j < colLength; j++ {
			if mat[i][j] == 1 {
				rows[i]++
				cols[j]++
			}
		}
	}
	for i := 0; i < rowLength; i++ {
		for j := 0; j < colLength; j++ {
			if mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1 {
				count++
			}
		}
	}
	return count
}

//
// func main() {
// mat := [][]int{
// []int{0,0,0,0,0},
// []int{1,0,0,0,0},
// []int{0,1,0,0,0},
// []int{0,0,1,0,0},
// []int{0,0,0,1,1},
// }
// fmt.Println(numSpecial(mat))
// }

// @lc code=end
