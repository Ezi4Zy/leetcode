/*
 * @lc app=leetcode.cn id=1413 lang=golang
 *
 * [1413] 逐步求和得到正数的最小值
 */

// @lc code=start
package main

func minStartValue(nums []int) int {
	minSum := 0
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		if sum < minSum {
			minSum = sum
		}
	}
	if minSum > 0 {
		return 1
	} else {
		return 1 - minSum
	}
}

// @lc code=end
