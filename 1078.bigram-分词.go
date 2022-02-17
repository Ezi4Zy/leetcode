/*
 * @lc app=leetcode.cn id=1078 lang=golang
 *
 * [1078] Bigram 分词
 */
package main

import (
	"strings"
)

// @lc code=start
func findOcurrences(text string, first string, second string) []string {
	ret := []string{}
	words := strings.Split(text, " ")
	for i := 0; i < len(words)-2; i++ {
		if words[i] == first && words[i+1] == second {
			ret = append(ret, words[i+2])
		}
	}
	return ret
}

// func main() {
// fmt.Println(findOcurrences("alice is a good girl she is a good student", "a", "good"),
// findOcurrences("we will we will rock you", "we", "will"))
// }

// @lc code=end
