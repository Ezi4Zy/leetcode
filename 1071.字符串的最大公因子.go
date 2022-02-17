/*
 * @lc app=leetcode.cn id=1071 lang=golang
 *
 * [1071] 字符串的最大公因子
 */
package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func gcdOfStrings(str1 string, str2 string) string {
	repeatedCount := 1
	minLength := len(str1)
	maxLength := len(str2)
	if len(str2) < minLength {
		minLength = len(str2)
		maxLength = len(str1)
	}
	for repeatedCount <= minLength {
		if minLength%repeatedCount == 0 {
			stepLength := minLength / repeatedCount
			if maxLength%stepLength == 0 {
				if strings.Repeat(str1[:stepLength], len(str1)/stepLength) == str1 && strings.Repeat(str1[:stepLength], len(str2)/stepLength) == str2 {
					return str1[:stepLength]
				}
			}
		}
		repeatedCount++
	}
	return ""
}

// func main() {
// fmt.Println(gcdOfStrings("ABCABC", "ABC"), gcdOfStrings("ABABAB", "ABAB"),
// gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"),
// gcdOfStrings("AA", "A"))
// }

// @lc code=end
