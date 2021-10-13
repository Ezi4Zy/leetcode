/*
 * @lc app=leetcode.cn id=1502 lang=golang
 *
 * [1502] 判断能否形成等差数列
 */

// @lc code=start
package main

import (
	"sort"
)

func canMakeArithmeticProgression(arr []int) bool {
	sort.Ints(arr)
	diff := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] != diff {
			return false
		}
	}
	return true
}

// func main() {
// fmt.Println(canMakeArithmeticProgression([]int{3, 5, 1}))
// fmt.Println(canMakeArithmeticProgression([]int{1, 2, 4}))
// }

// @lc code=end
