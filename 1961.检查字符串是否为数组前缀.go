/*
 * @lc app=leetcode.cn id=1961 lang=golang
 *
 * [1961] 检查字符串是否为数组前缀
 */

// package main

// import "fmt"

// @lc code=start
func isPrefixString(s string, words []string) bool {
	sIndex := 0
	for _, word := range words {
		for i, _ := range word {
			if word[i] != s[sIndex] {
				return false
			}
			sIndex++
			if sIndex == len(s) {
				return i == len(word)-1
			}
		}
	}
	return false
}

// func main() {
// fmt.Println(isPrefixString("iloveleetcode", []string{
// "i",
// "love",
// "leetcode",
// "apples",
// }))

// fmt.Println(isPrefixString("iloveleetcode", []string{
// "apples",
// "i",
// "love",
// "leetcode",
// }))

// fmt.Println(isPrefixString("a", []string{
// "aa",
// "i",
// "love",
// "leetcode",
// }))
// }

// @lc code=end
