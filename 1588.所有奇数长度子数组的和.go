/*
 * @lc app=leetcode.cn id=1588 lang=golang
 *
 * [1588] 所有奇数长度子数组的和
 */

// @lc code=start
package main

func sumOddLengthSubarrays(arr []int) int {
	step := 1
	sum := 0
	for step <= len(arr) {
		for i := 0; i <= len(arr)-step; i++ {
			for j := i; j < i+step; j++ {
				sum += arr[j]
			}
		}
		step += 2
	}
	return sum
}

// @lc code=end
