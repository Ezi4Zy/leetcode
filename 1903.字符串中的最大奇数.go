/*
 * @lc app=leetcode.cn id=1903 lang=golang
 *
 * [1903] 字符串中的最大奇数
 */

// @lc code=start
// package leetcode

func largestOddNumber(num string) string {
	n := []byte(num)
	oddNumberMap := map[byte]bool{'1': true, '3': true, '5': true, '7': true, '9': true}
	for i := len(n) - 1; i >= 0; i-- {
		if _, ok := oddNumberMap[n[i]]; ok {
			return string(n[:i+1])
		}
	}
	return ""

}

// @lc code=end
