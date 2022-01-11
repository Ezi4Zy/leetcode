/*
 * @lc app=leetcode.cn id=1346 lang=golang
 *
 * [1346] 检查整数及其两倍数是否存在
 */
package main

import (
	"sort"
)

// @lc code=start
func checkIfExist(arr []int) bool {
	sort.Ints(arr)
	for i := 0; i < len(arr)-1; i++ {
		half := 0
		if arr[i] < 0 {
			if arr[i]%2 == 0 {
				half = arr[i] / 2
			} else {
				continue
			}
		} else {
			half = arr[i] * 2
		}
		for j := i + 1; j < len(arr); j++ {
			if arr[j] < half {
				continue
			}
			if arr[j] == half {
				return true
			} else {
				break
			}
		}
	}
	return false
}

// func main() {
// fmt.Print(checkIfExist([]int{10, 2, 5, 3}))
// fmt.Print(checkIfExist([]int{7, 1, 14, 11}))
// fmt.Print(checkIfExist([]int{3, 1, 7, 11}))
// fmt.Print(checkIfExist([]int{-10, 12, -20, -8, 15}))
// }

// @lc code=end
