/*
 * @lc app=leetcode.cn id=1816 lang=golang
 *
 * [1816] 截断句子
 */

// @lc code=start
// package main
//
// import "fmt"

func truncateSentence(s string, k int) string {
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			k--
		}
		if k == 0 {
			return s[:i]
		}
	}
	return s
}

// func main() {
// fmt.Println(truncateSentence("What is the solution to this problem", 20))
// }

// @lc code=end
