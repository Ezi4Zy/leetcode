/*
 * @lc app=leetcode.cn id=1941 lang=golang
 *
 * [1941] 检查是否所有字符出现次数相同
 */
package main

// @lc code=start
func areOccurrencesEqual(s string) bool {
	counter := make([]int, 26)
	for i := 0; i < len(s); i++ {
		counter[s[i]-'a']++
	}
	count := counter[s[0]-'a']
	for _, c := range counter {
		if c != 0 && c != count {
			return false
		}
	}
	return true
}

// @lc code=end
