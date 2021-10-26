/*
 * @lc app=leetcode.cn id=1370 lang=golang
 *
 * [1370] 上升下降字符串
 */

// @lc code=start
package main

func sortString(s string) string {
	counter := make([]int, 26)
	ret := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		counter[s[i]-'a']++
	}
	charsIndex := 0
	index := 0
	for index < len(s) {
		realIndex := charsIndex % (52)
		if realIndex >= 26 {
			realIndex = 51 - realIndex
		}
		if counter[realIndex] > 0 {
			ret[index] = byte('a' + realIndex)
			index++
			counter[realIndex]--
		}
		charsIndex++
	}
	return string(ret)
}

// @lc code=end
