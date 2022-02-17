/*
 * @lc app=leetcode.cn id=1051 lang=golang
 *
 * [1051] 高度检查器
 */
package main

import (
	"sort"
)

// @lc code=start
func heightChecker(heights []int) int {
	excepted := make([]int, len(heights))
	for i := 0; i < len(heights); i++ {
		excepted[i] = heights[i]
	}
	sort.Ints(excepted)
	count := 0
	for i := 0; i < len(heights); i++ {
		if heights[i] != excepted[i] {
			count++
		}
	}
	return count
}

// func main() {
// fmt.Println(heightChecker([]int{1, 1, 4, 2, 1, 3}))
// }

// @lc code=end
