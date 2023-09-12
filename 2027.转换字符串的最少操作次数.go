/*
 * @lc app=leetcode.cn id=2027 lang=golang
 *
 * [2027] 转换字符串的最少操作次数
 */

package main

import "fmt"

// @lc code=start
func minimumMoves(s string) int {
	count := 0
	index := 0
	for index < len(s) {
		if s[index] == 'X' {
			count++
			index += 3
		} else {
			index++
		}
	}
	return count
}

// @lc code=end

func main() {
	fmt.Println(minimumMoves("XXX"))
	fmt.Println(minimumMoves("XXOX"))
	fmt.Println(minimumMoves("OOOO"))
}
