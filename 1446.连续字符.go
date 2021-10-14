/*
 * @lc app=leetcode.cn id=1446 lang=golang
 *
 * [1446] 连续字符
 */

// @lc code=start
package main

func maxPower(s string) int {
	ret := 1
	cur := 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			cur++
			if cur > ret {
				ret = cur
			}
		} else {
			cur = 1
		}
	}
	return ret
}

// @lc code=end
