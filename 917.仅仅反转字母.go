/*
 * @lc app=leetcode.cn id=917 lang=golang
 *
 * [917] 仅仅反转字母
 */
package main

import (
	"unicode"
)

// @lc code=start
func reverseOnlyLetters(s string) string {
	b := []byte(s)
	start := 0
	end := len(b) - 1
	for start < end {
		for start < end && !unicode.IsLetter(rune(s[start])) {
			start++
		}
		for end > start && !unicode.IsLetter(rune(s[end])) {
			end--
		}
		if start < end {
			b[start], b[end] = b[end], b[start]
			start++
			end--
		}
	}
	return string(b)
}

// func main() {
// fmt.Println(reverseOnlyLetters("ab-cd"), reverseOnlyLetters("a-bC-dEf-ghIj"), reverseOnlyLetters("Test1ng-Leet=code-Q!"))
// }

// @lc code=end
