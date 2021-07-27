/*
 * @lc app=leetcode.cn id=1784 lang=golang
 *
 * [1784] 检查二进制字符串字段
 */

// @lc code=start
func checkOnesSegment(s string) bool {
	zeroStart := 1
	for zeroStart < len(s) {
		if s[zeroStart] != s[0] {
			break
		}
		zeroStart++
	}
	for zeroStart < len(s) {
		if s[zeroStart] == s[0] {
			return false
		}
		zeroStart++
	}
	return true

}

// @lc code=end

