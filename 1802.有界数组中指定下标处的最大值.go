/*
 * @lc app=leetcode.cn id=1802 lang=golang
 *
 * [1802] 有界数组中指定下标处的最大值
 */

// @lc code=start
func maxValue(n int, index int, maxSum int) int {
	ret := 1
	maxSum -= n
	left := index
	right := index
	for maxSum >= right-left+1 {
		if left == 0 && right == n-1 {
			ret += maxSum / n
			return ret
		}
		ret += 1
		maxSum -= right - left + 1
		if left > 0 {
			left -= 1
		}
		if right < n-1 {
			right += 1
		}
	}
	return ret
}

// @lc code=end
