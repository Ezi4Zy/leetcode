/*
 * @lc app=leetcode.cn id=1636 lang=golang
 *
 * [1636] 按照频率将数组升序排序
 */

// @lc code=start
package main

import (
	"sort"
)

type intList []int

var counter map[int]int

func (s intList) Len() int {
	return len(s)
}
func (s intList) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s intList) Less(i, j int) bool {
	if counter[s[i]] == counter[s[j]] {
		return s[i] > s[j]
	} else {
		return counter[s[i]] < counter[s[j]]
	}
}

func frequencySort(nums []int) []int {
	counter = make(map[int]int)
	for i := 0; i < len(nums); i++ {
		counter[nums[i]]++
	}
	sort.Sort(intList(nums))
	return nums
}

//
// func main() {
// fmt.Println(frequencySort([]int{1, 1, 2, 2, 2, 3}))
// fmt.Println(frequencySort([]int{2, 3, 1, 3, 2}))
// fmt.Println(frequencySort([]int{-1, 1, -6, 4, 5, -6, 1, 4, 1}))
// }

// @lc code=end
