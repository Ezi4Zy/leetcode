/*
 * @lc app=leetcode.cn id=1886 lang=golang
 *
 * [1886] 判断矩阵经轮转后是否一致
 */

// @lc code=start
// package leetcode

func rotate(mat [][]int) [][]int {
	n := len(mat)
	ret := make([][]int, n)
	for i := 0; i < n; i++ {
		ret[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			ret[j][n-1-i] = mat[i][j]
		}
	}
	return ret
}

func equal(mat [][]int, target [][]int) bool {
	n := len(mat)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] != target[i][j]{
				return false
			}
		}
	}
	return true
}

func findRotation(mat [][]int, target [][]int) bool {
	for i := 0; i < 4; i++ {
		mat = rotate(mat)
		if equal(mat, target) {
			return true
		}
	}
	return false

}

// @lc code=end
