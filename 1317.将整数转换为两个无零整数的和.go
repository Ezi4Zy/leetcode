/*
 * @lc app=leetcode.cn id=1317 lang=golang
 *
 * [1317] 将整数转换为两个无零整数的和
 */
package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func getNoZeroIntegers(n int) []int {
	for first := 1; first < n; first++ {
		if !(strings.Contains(fmt.Sprint(first), "0") || strings.Contains(fmt.Sprint(n-first), "0")) {
			return []int{first, n - first}
		}
	}
	return []int{}
}

// func main() {
// fmt.Println(getNoZeroIntegers(11))
// fmt.Println(getNoZeroIntegers(2))
// fmt.Println(getNoZeroIntegers(10000))
// fmt.Println(getNoZeroIntegers(69))
// }

// @lc code=end
