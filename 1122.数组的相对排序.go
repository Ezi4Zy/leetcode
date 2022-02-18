/*
 * @lc app=leetcode.cn id=1122 lang=golang
 *
 * [1122] 数组的相对排序
 */
package main

import (
	"sort"
)

// @lc code=start
func relativeSortArray(arr1 []int, arr2 []int) []int {
	sort.Slice(arr1, func(i, j int) bool {
		index1 := len(arr2)
		index2 := len(arr2)
		for m := 0; m < len(arr2); m++ {
			if arr2[m] == arr1[i] {
				index1 = m
			}
			if arr2[m] == arr1[j] {
				index2 = m
			}
		}
		if index1 == len(arr2) && index2 == len(arr2) {
			return arr1[i] < arr1[j]
		} else {
			return index1 < index2
		}
	})
	return arr1
}

// func main() {
// fmt.Println(relativeSortArray([]int{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19}, []int{2, 1, 4, 3, 9, 6}),
// relativeSortArray([]int{28, 6, 22, 8, 44, 17}, []int{22, 28, 8, 6}))
// }

// @lc code=end
