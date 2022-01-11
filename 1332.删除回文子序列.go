/*
 * @lc app=leetcode.cn id=1332 lang=golang
 *
 * [1332] 删除回文子序列
 */
package main

// @lc code=start
func removePalindromeSub(s string) int {
	start := 0
	end := len(s) - 1
	if end < start {
		return 0
	}
	for start <= end {
		if s[start] != s[end] {
			return 2
		} else {
			start++
			end--
		}
	}
	return 1
}

// @lc code=end
