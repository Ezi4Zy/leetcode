/*
 * @lc app=leetcode.cn id=696 lang=golang
 *
 * [696] 计数二进制子串
 */

// @lc code=start
// package leetcode

func countBinarySubstrings(s string) int {
	pre := 0
	next := 0
	ret := 0
	preChar := s[0]
	n := len(s)
	for i := 0; i < n; {
		if s[i] == preChar {
			pre++
			i++
		} else {
			for i < n && s[i] != preChar {
				next++
				i++
			}
			if pre > next {
				ret += next
			} else {
				ret += pre
			}
			next, pre = 0, next
			preChar = s[i-1]
		}
	}
	return ret

}

// @lc code=end
