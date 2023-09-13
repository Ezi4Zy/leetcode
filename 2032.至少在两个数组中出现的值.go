/*
 * @lc app=leetcode.cn id=2032 lang=golang
 *
 * [2032] 至少在两个数组中出现的值
 */
package main

import "fmt"

// @lc code=start
func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	ret := []int{}
	mask := map[int]int{}
	for i, nums := range [][]int{nums1, nums2, nums3} {
		for _, x := range nums {
			mask[x] |= 1 << i
		}
	}
	for x, m := range mask {
		if m&(m-1) > 0 {
			ret = append(ret, x)
		}
	}
	return ret

}

// @lc code=end

func main() {
	fmt.Println(twoOutOfThree([]int{1, 1, 3, 2}, []int{2, 3}, []int{3}))
	fmt.Println(twoOutOfThree([]int{3, 1}, []int{2, 3}, []int{1, 2}))
	fmt.Println(twoOutOfThree([]int{1, 2, 2}, []int{4, 3, 3}, []int{5}))
}
