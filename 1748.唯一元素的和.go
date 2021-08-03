/*
 * @lc app=leetcode.cn id=1748 lang=golang
 *
 * [1748] 唯一元素的和
 */

// @lc code=start
package main

func sumOfUnique(nums []int) int {
	ret := 0
	numCount := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		numCount[nums[i]]++
	}
	for k, v := range numCount {
		if v == 1 {
			ret += k
		}
	}
	return ret
}

// @lc code=end
