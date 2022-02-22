/*
 * @lc app=leetcode.cn id=1929 lang=golang
 *
 * [1929] 数组串联
 */
package main

// @lc code=start
func getConcatenation(nums []int) []int {
	ret := make([]int, len(nums)*2)
	for i := 0; i < len(nums); i++ {
		ret[i] = nums[i]
		ret[i+len(nums)] = ret[i]
	}
	return ret
}

// @lc code=end
