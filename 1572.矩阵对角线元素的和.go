/*
 * @lc app=leetcode.cn id=1572 lang=golang
 *
 * [1572] 矩阵对角线元素的和
 */

// @lc code=start
package main

func diagonalSum(mat [][]int) int {
	ret := 0
	length := len(mat)
	for i := 0; i < length; i++ {
		ret += mat[i][i] + mat[i][length-i-1]
	}
	if length%2 == 1 {
		return ret - mat[length/2][length/2]
	} else {
		return ret
	}
}

// func main() {
// mat := [][]int{
// []int{1, 2, 3},
// []int{4, 5, 6},
// []int{7, 8, 9},
// }
// fmt.Println(diagonalSum(mat))
// mat1 := [][]int{
// []int{7, 3, 1, 9},
// []int{3, 4, 6, 9},
// []int{6, 9, 6, 6},
// []int{9, 5, 8, 5},
// }
// fmt.Println(diagonalSum(mat1))
// }

// @lc code=end
