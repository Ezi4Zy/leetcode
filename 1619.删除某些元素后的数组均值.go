/*
 * @lc app=leetcode.cn id=1619 lang=golang
 *
 * [1619] 删除某些元素后的数组均值
 */

// @lc code=start
package main

import (
	"sort"
)

type intList []int

func (s intList) Len() int {
	return len(s)
}
func (s intList) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s intList) Less(i, j int) bool {
	return s[i] < s[j]
}

func trimMean(arr []int) float64 {
	sort.Sort(intList(arr))
	deleteCount := len(arr) / 20
	sum := 0
	for i := deleteCount; i < len(arr)-deleteCount; i++ {
		sum += arr[i]
	}
	return float64(sum) / float64(len(arr)-2*deleteCount)
}

// func main() {
// fmt.Println(trimMean([]int{1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3}))
// }

// @lc code=end
