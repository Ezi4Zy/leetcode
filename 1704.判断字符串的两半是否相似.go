/*
 * @lc app=leetcode.cn id=1704 lang=golang
 *
 * [1704] 判断字符串的两半是否相似
 */

// @lc code=start
package main

func halvesAreAlike(s string) bool {
	frontCount := 0
	endCount := 0
	charMap := map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
		'A': true,
		'E': true,
		'I': true,
		'O': true,
		'U': true,
	}
	for i := 0; i < len(s)/2; i++ {
		if b, ok := charMap[s[i]]; b && ok {
			frontCount++
		}
	}
	for i := len(s) / 2; i < len(s); i++ {
		if b, ok := charMap[s[i]]; b && ok {
			endCount++
		}
	}

	return frontCount == endCount

}

// @lc code=end
