/*
 * @lc app=leetcode.cn id=1356 lang=golang
 *
 * [1356] 根据数字二进制下 1 的数目排序
 */
package main

import (
	"sort"
)

// @lc code=start
func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		counti := 0
		countj := 0
		tempi, tempj := arr[i], arr[j]
		valueLess := tempi < tempj
		for tempi > 0 {
			counti += tempi % 2
			tempi = tempi / 2
		}
		for tempj > 0 {
			countj += tempj % 2
			tempj = tempj / 2
		}
		if counti == countj {
			return valueLess
		} else {
			return counti < countj
		}
	})
	return arr
}

// func main() {
// fmt.Println(sortByBits([]int{0, 1, 2, 3, 4, 5, 6, 7, 8}))
// fmt.Println(sortByBits([]int{1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1}))
// fmt.Println(sortByBits([]int{10000, 10000}))
// fmt.Println(sortByBits([]int{2, 3, 5, 7, 11, 13, 17, 19}))
// fmt.Println(sortByBits([]int{10, 100, 1000, 10000}))
// }

// @lc code=end
