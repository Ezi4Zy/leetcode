/*
 * @lc app=leetcode.cn id=1403 lang=golang
 *
 * [1403] 非递增顺序的最小子序列
 */

// @lc code=start
package main

import "sort"

func minSubsequence(nums []int) []int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}
	cur := 0
	ret := []int{}
	for i := len(nums) - 1; i >= 0; i-- {
		cur += nums[i]
		ret = append(ret, nums[i])
		if cur > sum/2 {
			break
		}
	}
	return ret
}

// @lc code=end
