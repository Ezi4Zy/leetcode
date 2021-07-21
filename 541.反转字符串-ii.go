/*
 * @lc app=leetcode.cn id=541 lang=golang
 *
 * [541] 反转字符串 II
 */

// @lc code=start
// package leetcode

func reverse(b []byte) {
	left := 0
	right := len(b) - 1
	for right > left {
		b[left], b[right] = b[right], b[left]
		left++
		right--
	}
}

func reverseStr(s string, k int) string {
	n := len(s)
	b := []byte(s)
	for i := 0; i < n; {
		if n-i < k {
			reverse(b[i:n])
		} else {
			reverse(b[i : i+k])
		}
		i += 2 * k
	}
	return string(b)

}

// @lc code=end
