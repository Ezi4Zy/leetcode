/*
 * @lc app=leetcode.cn id=1365 lang=golang
 *
 * [1365] 有多少小于当前数字的数字
 */

// @lc code=start
package main

func smallerNumbersThanCurrent(nums []int) []int {
	ret := make([]int, len(nums))
	counter := make([]int, 101)
	for i := 0; i < len(nums); i++ {
		counter[nums[i]]++
	}
	for i := 1; i < 101; i++ {
		counter[i] += counter[i-1]
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			ret[i] = counter[nums[i]-1]
		}
	}
	return ret
}

// @lc code=end
