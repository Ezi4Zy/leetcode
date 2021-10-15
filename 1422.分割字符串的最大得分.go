/*
 * @lc app=leetcode.cn id=1422 lang=golang
 *
 * [1422] 分割字符串的最大得分
 */

// @lc code=start
package main

func maxScore(s string) int {
	left := 0
	right := 0
	if s[0] == '0' {
		left = 1
	}
	for i := 1; i < len(s); i++ {
		if s[i] == '1' {
			right++
		}
	}
	score := left + right
	for i := 1; i < len(s)-1; i++ {
		if s[i] == '0' {
			left++
		} else {
			right--
		}
		if left+right > score {
			score = left + right
		}
	}
	return score
}

// func main() {
// fmt.Println(maxScore("011101"))
// fmt.Println(maxScore("00111"))
// fmt.Println(maxScore("1111"))
// }

// @lc code=end
