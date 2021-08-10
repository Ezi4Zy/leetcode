/*
 * @lc app=leetcode.cn id=1608 lang=golang
 *
 * [1608] 特殊数组的特征值
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

func specialArray(nums []int) int {
	sort.Sort(intList(nums))

	for i := 0; i < len(nums); i++ {
		if nums[i] >= len(nums)-i && (i > 0 && nums[i-1] < len(nums)-i || i == 0) {
			return len(nums) - i
		}
	}
	return -1

}

//
// func main() {
// fmt.Println(specialArray([]int{3, 5}))
// fmt.Println(specialArray([]int{0, 0}))
// fmt.Println(specialArray([]int{0, 4, 3, 0, 4}))
// fmt.Println(specialArray([]int{3, 6, 7, 7, 0}))
// }

// @lc code=end
