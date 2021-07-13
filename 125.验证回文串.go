/*
 * @lc app=leetcode.cn id=125 lang=golang
 *
 * [125] 验证回文串
 */

// @lc code=start
// package leetcode

import (
	"unicode"
)
func isPalindrome(s string) bool {
	r := []rune(s)
	start := 0
	end := len(r) - 1
	for {
		for start < end && !(unicode.IsLetter(r[start]) || unicode.IsDigit(r[start])){
			start += 1
		}
		for start < end && !(unicode.IsLetter(r[end]) || unicode.IsDigit(r[end])){
			end -= 1
		}
		if start >= end {
			break
		}
		if unicode.IsLetter(r[start]) {
			r[start] = unicode.ToLower(r[start])
		}
		if unicode.IsLetter(r[end]){
			r[end] = unicode.ToLower(r[end])
		}
		if r[start] != r[end] {
			return false
		}else {
			start += 1
			end -= 1
		}

	}
	return true
}
// @lc code=end

