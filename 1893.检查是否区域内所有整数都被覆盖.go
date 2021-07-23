/*
 * @lc app=leetcode.cn id=1893 lang=golang
 *
 * [1893] 检查是否区域内所有整数都被覆盖
 */

// @lc code=start
// package main
//
// import "fmt"

func isCovered(ranges [][]int, left int, right int) bool {

	if left > right {
		return true
	}
	for i := 0; i < len(ranges); i++ {
		start, end := ranges[i][0], ranges[i][1]
		if start > right || end < left {
			return isCovered(ranges[i+1:], left, right)
		} else {
			return isCovered(ranges[i+1:], left, start-1) && isCovered(ranges[i+1:], end+1, right)

		}
	}
	return false

}

//
// func main() {
// ranges := [][]int{{1, 1}}
// isCovered(ranges, 1, 50)
// }

// @lc code=end
